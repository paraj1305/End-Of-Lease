# 14 — Email Notifications

## Overview
Email notifications are sent automatically for key booking events. The system uses Django's email framework with SMTP.

---

## Email Events

| Event | Recipient | Trigger |
|-------|-----------|---------|
| Booking Confirmation | Customer | Stripe `payment_intent.succeeded` webhook |
| New Booking Alert | Admin | Same as above (optional, configurable) |
| Booking Cancellation | Customer | Admin cancels booking |

---

## Customer Booking Confirmation Email

### Subject
`Your Cleaning Booking is Confirmed — Ref: EOL-2026-XXXXXX`

### Content
- Branded header with logo
- ✅ "Your booking is confirmed!" headline
- Booking reference number
- Package name
- Selected add-ons (if any)
- Date and time
- Service address
- Amount paid today (deposit)
- Remaining amount (with note: payable on the day of cleaning)
- Business contact information
- "If you need to change or cancel your booking, please contact us at: [email/phone]"
- Footer with Privacy Policy and Terms links

### Template Path
`templates/emails/booking_confirmation.html`
`templates/emails/booking_confirmation.txt` (plain text fallback)

---

## Email Configuration

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@domain.com.au')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@domain.com.au')
```

---

## Phase 2 Email Enhancements
- SMS confirmation (via Twilio or similar)
- WhatsApp confirmation
- Booking reminder (1 day before)
- Post-cleaning review request

---

## Related Documents
- `07-booking-management.md`
- `09-payments.md`
