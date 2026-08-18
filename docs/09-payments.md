# 09 — Payments (Stripe)

## Overview
The platform uses **Stripe** as the payment gateway for collecting the 10% booking deposit. The remaining 90% is collected separately by the business on the day of cleaning.

---

## Payment Flow

```
Customer completes booking summary
        │
        ▼
Server creates Stripe PaymentIntent
(amount = 10% of subtotal, currency = AUD)
        │
        ▼
Customer sees Stripe payment form (Stripe Elements or Checkout)
        │
        ▼
Customer enters card details and submits
        │
        ├── Payment fails → Error shown → Customer can retry
        │
        └── Payment succeeds (client-side)
                │
                ▼
        Stripe sends webhook → payment_intent.succeeded
                │
                ▼
        Server verifies webhook signature
                │
                ▼
        Booking status → CONFIRMED
        Date marked as booked in database
        Confirmation email sent
        Confirmation page shown
```

---

## Deposit Calculation

```python
def calculate_deposit(package_price, addons_total, deposit_pct=10):
    """
    Calculate the 10% deposit amount.
    
    Args:
        package_price: Decimal — price of the selected package
        addons_total: Decimal — sum of all selected add-on prices
        deposit_pct: int — deposit percentage (default 10, configurable from settings)
    
    Returns:
        dict with subtotal, deposit_amount, remaining_amount
    """
    subtotal = package_price + addons_total
    deposit_amount = (subtotal * deposit_pct / 100).quantize(Decimal('0.01'))
    remaining_amount = subtotal - deposit_amount
    return {
        'subtotal': subtotal,
        'deposit_amount': deposit_amount,
        'remaining_amount': remaining_amount,
    }
```

> **Open question:** Is the 10% calculated on the package price only, or package + add-ons? Assumed: **package + add-ons** (full subtotal). Confirm with client.

---

## Stripe Integration

### Settings Required

```python
# settings.py (use environment variables — never hardcode)
STRIPE_PUBLIC_KEY = os.environ['STRIPE_PUBLIC_KEY']
STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']
STRIPE_WEBHOOK_SECRET = os.environ['STRIPE_WEBHOOK_SECRET']
STRIPE_CURRENCY = 'aud'  # Confirm with client
```

### Creating a PaymentIntent

```python
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

intent = stripe.PaymentIntent.create(
    amount=int(deposit_amount * 100),  # Stripe uses cents
    currency=settings.STRIPE_CURRENCY,
    metadata={
        'booking_id': str(booking.pk),
        'booking_reference': booking.reference,
    }
)
```

### Webhook Endpoint

```
POST /webhooks/stripe/
```

- Verifies Stripe signature using `STRIPE_WEBHOOK_SECRET`
- Handles: `payment_intent.succeeded`, `payment_intent.payment_failed`
- Must respond with HTTP 200 quickly (< 10 seconds)
- All business logic (status update, email) runs after responding if possible, or asynchronously

### Webhook Handler Logic

```python
def handle_payment_succeeded(payment_intent):
    booking_id = payment_intent['metadata']['booking_id']
    with transaction.atomic():
        booking = Booking.objects.select_for_update().get(pk=booking_id)
        if booking.status == Booking.Status.DRAFT:
            if not is_date_available(booking.booking_date):
                # Race condition: another booking won — refund this one
                initiate_stripe_refund(payment_intent['id'])
                booking.status = Booking.Status.CANCELLED
                booking.save()
                send_race_condition_cancellation_email(booking)
            else:
                booking.status = Booking.Status.CONFIRMED
                booking.payment_status = 'paid'
                booking.stripe_payment_intent_id = payment_intent['id']
                booking.deposit_paid_at = timezone.now()
                booking.save()
                send_booking_confirmation_email(booking)
```

---

## Payment Status Values

| Status | Description |
|--------|-------------|
| `pending` | Booking created, payment not yet initiated |
| `paid` | Deposit payment confirmed by Stripe |
| `failed` | Payment failed |
| `refunded` | Deposit refunded (admin-initiated or race condition) |

---

## Admin Payment View

- Admin can view payment status for each booking
- Admin can see: Stripe PaymentIntent ID, amount paid, date paid
- Admin does NOT refund through this UI in MVP (use Stripe Dashboard for refunds)
- Phase 2: admin-initiated refunds through the platform

---

## Security Requirements

- All Stripe keys stored in environment variables (never in code or git)
- CSRF protection on all payment-related views
- Stripe webhook signature verification is MANDATORY — reject any request that fails verification
- Never trust client-side payment amounts — always calculate server-side
- Use HTTPS in production

---

## Stripe Test Cards (for development)

| Card Number | Scenario |
|-------------|---------|
| 4242 4242 4242 4242 | Payment succeeds |
| 4000 0000 0000 0002 | Card declined |
| 4000 0025 0000 3155 | 3D Secure required |

Expiry: any future date. CVV: any 3 digits. ZIP: any.

---

## Related Documents
- `03-user-booking-flow.md`
- `07-booking-management.md`
- `08-availability-and-calendar.md`
- `14-email-notifications.md`
