# 15 — Django Project Structure

## Overview
This document defines the Django project structure and app layout.

---

## Project Layout

```
eol_cleaning/                        # Django project root
├── manage.py
├── requirements.txt
├── .env.example                     # Environment variable template (never commit .env)
├── .gitignore
├── README.md
│
├── config/                          # Django project settings package
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py                  # Common settings
│   │   ├── development.py           # Dev settings (DEBUG=True, SQLite)
│   │   └── production.py            # Production settings (PostgreSQL, S3, etc.)
│   ├── urls.py                      # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/
│   ├── bookings/                    # Core booking logic
│   │   ├── models.py                # CleaningPackage, AddOnService, Booking, TimeSlot, BlockedDate
│   │   ├── views.py                 # Booking flow views (step by step)
│   │   ├── forms.py                 # Booking forms
│   │   ├── urls.py
│   │   ├── admin.py                 # Django admin configuration
│   │   ├── services/
│   │   │   ├── availability.py      # Date availability logic
│   │   │   ├── pricing.py           # Deposit calculation
│   │   │   ├── email.py             # Email sending
│   │   │   └── google_calendar.py   # PHASE 2 ONLY — placeholder file, not implemented
│   │   ├── api/
│   │   │   ├── views.py             # HTMX/JSON API endpoints (availability, price calc)
│   │   │   └── urls.py
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── cleanup_draft_bookings.py
│   │   ├── templates/
│   │   │   └── bookings/
│   │   │       ├── step1_package.html
│   │   │       ├── step2_addons.html
│   │   │       ├── step3_datetime.html
│   │   │       ├── step4_details.html
│   │   │       ├── step5_review.html
│   │   │       ├── payment.html
│   │   │       └── confirmation.html
│   │   └── migrations/
│   │
│   ├── public/                      # Public-facing pages (non-booking)
│   │   ├── models.py                # (Minimal — content may be static or simple models)
│   │   ├── views.py                 # Home, Services, About, Contact, FAQ views
│   │   ├── urls.py
│   │   ├── templates/
│   │   │   └── public/
│   │   │       ├── home.html        # Landing page
│   │   │       ├── services.html
│   │   │       ├── about.html
│   │   │       ├── contact.html
│   │   │       ├── faq.html
│   │   │       ├── privacy.html
│   │   │       ├── terms.html
│   │   │       └── cancellation_policy.html
│   │   └── migrations/
│   │
│   └── payments/                    # Stripe payment handling
│       ├── views.py                 # Stripe Checkout / webhook handler
│       ├── urls.py
│       ├── services.py
│       └── migrations/
│
├── templates/                       # Global templates
│   ├── base.html                    # Base template with head, nav, footer, PWA tags
│   ├── base_booking.html            # Base for booking flow (progress indicator)
│   ├── offline.html                 # PWA offline fallback
│   ├── 404.html
│   ├── 500.html
│   └── emails/
│       ├── booking_confirmation.html
│       └── booking_confirmation.txt
│
├── static/                          # Static files
│   ├── css/
│   │   ├── main.css                 # Main stylesheet
│   │   ├── landing.css              # Landing page specific styles
│   │   ├── booking.css              # Booking flow styles
│   │   └── admin_custom.css         # Admin customizations
│   ├── js/
│   │   ├── main.js                  # Global JS (nav, animations, PWA install)
│   │   ├── scroll-video.js          # Scroll-driven video controller
│   │   ├── before-after-slider.js   # Before/after image slider
│   │   ├── booking-calendar.js      # Custom date picker
│   │   ├── booking-addons.js        # Add-on selection + running total
│   │   └── sw.js                    # Service Worker
│   ├── images/
│   │   ├── hero-poster.webp         # Hero video poster (placeholder)
│   │   ├── before-*.webp            # Before images (placeholders)
│   │   ├── after-*.webp             # After images (placeholders)
│   │   └── og-image.jpg             # Open Graph image
│   ├── video/
│   │   ├── hero-transformation.mp4  # PLACEHOLDER — final video from client
│   │   └── hero-transformation.webm # WebM version for better browser support
│   ├── icons/                       # PWA icons
│   │   ├── icon-72.png
│   │   ├── icon-96.png
│   │   ├── icon-128.png
│   │   ├── icon-144.png
│   │   ├── icon-152.png
│   │   ├── icon-192.png
│   │   ├── icon-384.png
│   │   └── icon-512.png
│   └── manifest.json                # Web App Manifest
│
└── media/                           # User-uploaded files (admin)
```

---

## Environment Variables Required

```bash
# .env.example

# Django
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=domain.com.au,www.domain.com.au

# Database (Production)
DATABASE_URL=postgres://user:password@host:5432/dbname

# Stripe
STRIPE_PUBLIC_KEY=pk_live_...
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
STRIPE_CURRENCY=aud

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=noreply@domain.com.au
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@domain.com.au
ADMIN_EMAIL=admin@domain.com.au

# Business Settings
BUSINESS_NAME=EOL Cleaning
DEPOSIT_PERCENTAGE=10

# Google Calendar (PHASE 2 — leave empty in MVP)
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_CALENDAR_ID=
GOOGLE_REFRESH_TOKEN=
```

---

## Related Documents
- `16-api-and-backend-architecture.md`
- `17-database-schema.md`
