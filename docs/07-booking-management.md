# 07 — Booking Management

## Overview
This document covers the Booking data model, status lifecycle, and admin management of bookings.

---

## Django Model

```python
# bookings/models.py

import uuid

class Booking(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'
        COMPLETED = 'completed', 'Completed'

    # Reference
    reference = models.CharField(max_length=20, unique=True, editable=False)
    # e.g., "EOL-2026-00042"

    # Package snapshot
    package = models.ForeignKey('CleaningPackage', on_delete=models.PROTECT)
    package_name_at_booking = models.CharField(max_length=100)
    package_price_at_booking = models.DecimalField(max_digits=8, decimal_places=2)

    # Pricing snapshot
    addons_total_at_booking = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    deposit_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
    deposit_amount = models.DecimalField(max_digits=8, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=8, decimal_places=2)

    # Scheduling
    booking_date = models.DateField()
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.PROTECT)

    # Customer details
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    service_address_street = models.CharField(max_length=255)
    service_address_suburb = models.CharField(max_length=100)
    service_address_postcode = models.CharField(max_length=10)
    service_address_state = models.CharField(max_length=50)
    special_instructions = models.TextField(blank=True)

    # Status & Payment
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    payment_status = models.CharField(max_length=50, default='pending')
    # e.g., 'pending', 'paid', 'refunded'
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True)
    stripe_session_id = models.CharField(max_length=255, blank=True)
    deposit_paid_at = models.DateTimeField(null=True, blank=True)

    # Admin notes
    admin_notes = models.TextField(blank=True)

    # Google Calendar (Phase 2)
    google_calendar_event_id = models.CharField(max_length=255, blank=True)
    # NOTE: This field is reserved for Phase 2 Google Calendar integration.
    # It is intentionally included in the model now to avoid future migrations.
    # Do not populate or depend on this field in MVP.

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-booking_date', '-created_at']

    def __str__(self):
        return f"{self.reference} — {self.customer_name} ({self.booking_date})"

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        super().save(*args, **kwargs)

    def _generate_reference(self):
        from django.utils import timezone
        year = timezone.now().year
        # Generate sequential number — implement with a counter or UUID fallback
        return f"EOL-{year}-{uuid.uuid4().hex[:6].upper()}"
```

---

## Booking Status Lifecycle

```
DRAFT
  │
  ├── Payment initiated → stays DRAFT
  │
  └── Stripe webhook: payment_intent.succeeded
          │
          ▼
      CONFIRMED ──────────────────────────────┐
          │                                    │
          │  (after cleaning job done)         │  (admin cancels)
          ▼                                    ▼
      COMPLETED                           CANCELLED
```

---

## Business Rules

1. A booking is created in `DRAFT` status before Stripe payment is processed.
2. Only Stripe webhooks (not frontend redirects) should set the status to `CONFIRMED` to ensure payment integrity.
3. A date is considered "booked" only when a `CONFIRMED` booking exists for it.
4. `DRAFT` bookings do NOT block a date for other customers.
5. `DRAFT` bookings older than 30 minutes with no payment should be cleaned up by a scheduled management command.
6. Booking reference is generated automatically (human-readable, unique).
7. All price fields are stored as snapshots at booking time — never re-computed from current prices.
8. The `google_calendar_event_id` field is present in the model but unused in MVP.

---

## TimeSlot Model

```python
class TimeSlot(models.Model):
    label = models.CharField(max_length=50)     # e.g., "9:00 AM"
    start_time = models.TimeField()             # e.g., 09:00
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'start_time']

    def __str__(self):
        return self.label
```

---

## Draft Cleanup Command

```python
# bookings/management/commands/cleanup_draft_bookings.py
# Runs via: python manage.py cleanup_draft_bookings
# Schedule via cron or Celery beat:
#   0 * * * *  → every hour
```

Deletes (or marks cancelled) `DRAFT` bookings older than 30 minutes.

---

## Related Documents
- `05-packages.md`
- `06-addons.md`
- `08-availability-and-calendar.md`
- `09-payments.md`
- `10-google-calendar.md` (Phase 2 only)
