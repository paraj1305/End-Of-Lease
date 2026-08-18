# 16 — API & Backend Architecture

## Overview
This document defines the backend architecture, URL endpoints, API design, and Django view patterns used throughout the platform.

---

## Architecture Overview

```
Browser / PWA
    │
    │  HTTP/HTTPS
    ▼
Django Application Server (Gunicorn / uvicorn)
    │
    ├── Public Views (SSR HTML — Django Templates + HTMX)
    │   ├── Landing Page
    │   ├── Services / Packages
    │   ├── About, Contact, FAQ
    │   └── Booking flow (steps 1–5)
    │
    ├── Payment Views
    │   ├── Stripe Payment Intent creation
    │   ├── Stripe Checkout redirect
    │   └── Stripe Webhook handler
    │
    ├── API Views (JSON — used by HTMX and JS)
    │   ├── /api/availability/
    │   ├── /api/price/
    │   └── /api/timeslots/
    │
    ├── Admin Views (Django Admin + custom views)
    │
    └── Webhook Handler (/webhooks/stripe/)
            │
    ┌───────┘
    │
    ▼
    Database (SQLite → PostgreSQL)
    │
    ├── CleaningPackage
    ├── AddOnService
    ├── Booking + BookingAddOn
    ├── TimeSlot
    └── BlockedDate
```

---

## URL Structure

### Public Pages
```
GET  /                         → Home / Landing page
GET  /services/                → Cleaning packages and services
GET  /about/                   → About us
GET  /contact/                 → Contact page
POST /contact/                 → Contact form submission
GET  /faq/                     → FAQ page
GET  /privacy/                 → Privacy Policy
GET  /terms/                   → Terms of Service
GET  /cancellation-policy/     → Cancellation Policy
GET  /offline.html             → PWA offline fallback (static)
GET  /sitemap.xml              → XML sitemap
GET  /robots.txt               → robots.txt
```

### Booking Flow
```
GET  /book/                    → Redirect to step 1
GET  /book/package/            → Step 1: Select package
POST /book/package/            → Save package selection to session
GET  /book/addons/             → Step 2: Select add-ons
POST /book/addons/             → Save add-on selection to session
GET  /book/datetime/           → Step 3: Select date & time
POST /book/datetime/           → Save date/time to session
GET  /book/details/            → Step 4: Enter customer details
POST /book/details/            → Save details to session
GET  /book/review/             → Step 5: Review summary
POST /book/review/             → Create draft Booking + redirect to payment
GET  /book/payment/            → Payment page (Stripe Elements)
POST /book/payment/            → Create Stripe PaymentIntent (AJAX)
GET  /book/confirmation/<ref>/ → Booking confirmation page
```

### Payment / Webhooks
```
POST /payments/create-intent/  → Create Stripe PaymentIntent (returns client_secret)
POST /webhooks/stripe/         → Stripe webhook handler
```

### API Endpoints (HTMX / JSON)
```
GET  /api/availability/?month=YYYY-MM     → Date status for calendar
GET  /api/timeslots/?date=YYYY-MM-DD      → Available time slots for date
POST /api/price/                          → Calculate price (package + add-ons)
GET  /api/packages/                       → Active packages (JSON)
GET  /api/addons/                         → Active add-ons (JSON)
```

---

## API Response Format

### GET /api/availability/

```json
{
  "month": "2026-02",
  "dates": {
    "2026-02-01": "available",
    "2026-02-02": "booked",
    "2026-02-03": "blocked",
    "2026-02-04": "available"
  }
}
```

### GET /api/timeslots/

```json
{
  "date": "2026-02-05",
  "slots": [
    {"id": 1, "label": "8:00 AM", "start_time": "08:00"},
    {"id": 2, "label": "10:00 AM", "start_time": "10:00"},
    {"id": 3, "label": "12:00 PM", "start_time": "12:00"}
  ]
}
```

### POST /api/price/

```json
// Request
{
  "package_id": 2,
  "addon_ids": [1, 3]
}

// Response
{
  "package_price": "350.00",
  "addons_total": "50.00",
  "subtotal": "400.00",
  "deposit_percentage": 10,
  "deposit_amount": "40.00",
  "remaining_amount": "360.00"
}
```

---

## Session-Based Booking State

During the booking flow, state is held in Django's session:

```python
# Session keys
request.session['booking'] = {
    'package_id': 2,
    'addon_ids': [1, 3],
    'booking_date': '2026-02-05',
    'time_slot_id': 2,
    'customer': {
        'name': 'John Smith',
        'email': 'john@example.com',
        'phone': '0412345678',
        'address_street': '12 Main St',
        'address_suburb': 'Parramatta',
        'address_postcode': '2150',
        'address_state': 'NSW',
        'notes': '',
    }
}
```

Session is cleared after a confirmed booking is created.

---

## Stripe Payment Intent Creation

```python
# payments/views.py

@require_POST
def create_payment_intent(request):
    """
    Creates a Stripe PaymentIntent for the current booking session.
    Returns the client_secret for Stripe Elements.
    """
    booking_data = request.session.get('booking')
    if not booking_data:
        return JsonResponse({'error': 'No booking session found'}, status=400)
    
    # Calculate price server-side (never trust client-side amounts)
    price_data = calculate_price(booking_data['package_id'], booking_data['addon_ids'])
    
    # Create provisional Booking record
    booking = create_draft_booking(request, booking_data, price_data)
    
    # Create Stripe PaymentIntent
    intent = stripe.PaymentIntent.create(
        amount=int(price_data['deposit_amount'] * 100),  # cents
        currency=settings.STRIPE_CURRENCY,
        metadata={
            'booking_id': str(booking.pk),
            'booking_reference': booking.reference,
        }
    )
    
    return JsonResponse({'client_secret': intent.client_secret})
```

---

## Stripe Webhook Handler

```python
# payments/views.py

@csrf_exempt
def stripe_webhook(request):
    """
    Handles Stripe webhook events.
    MUST verify signature before processing.
    """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)
    
    if event['type'] == 'payment_intent.succeeded':
        handle_payment_succeeded(event['data']['object'])
    elif event['type'] == 'payment_intent.payment_failed':
        handle_payment_failed(event['data']['object'])
    
    return HttpResponse(status=200)
```

---

## HTMX Usage

HTMX is used for partial page updates without full page reloads:
- Calendar date selection → load available time slots
- Add-on toggle → update running total
- Admin: block/unblock dates inline
- Admin: status updates

Example:
```html
<!-- Date selected → load time slots -->
<div hx-get="/api/timeslots/?date=2026-02-05"
     hx-trigger="click"
     hx-target="#timeslot-container"
     hx-swap="innerHTML">
  Select a date
</div>
```

---

## Security

| Concern | Mitigation |
|---------|-----------|
| CSRF | Django CSRF middleware on all POST views |
| Stripe webhook | Signature verification (reject all others) |
| Input validation | Django forms + server-side validation on every step |
| XSS | Django template auto-escaping |
| SQL injection | Django ORM (parameterized queries) |
| Secrets | Environment variables, never in code/git |
| HTTPS | Required in production |
| Admin access | Django auth system, strong password required |
| Session fixation | Django session rotation on login |

---

## Google Calendar (Phase 2)

> The `google_calendar.py` service file is created as a placeholder during MVP but contains NO implementation.
> Phase 2 will implement the Google Calendar push sync.
> See `10-google-calendar.md`.

---

## Related Documents
- `15-django-project-structure.md`
- `08-availability-and-calendar.md`
- `09-payments.md`
- `07-booking-management.md`
