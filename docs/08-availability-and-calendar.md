# 08 — Availability & Calendar

## Overview
This document defines how date/time availability works for the booking system. The application's own database is the **source of truth** for all availability. Google Calendar is **NOT** part of the MVP — it is a Phase 2 feature.

---

## Core Rules

1. **One booking per day** — only one confirmed booking is allowed per calendar date.
2. A date becomes **Booked** automatically when a `CONFIRMED` booking is created for that date.
3. Admin can **Block** any date manually, making it unavailable regardless of bookings.
4. Admin can **Unblock** a previously blocked date.
5. `DRAFT` bookings do NOT reserve or block a date.
6. The application database is always the authoritative source — Google Calendar (Phase 2) is a read-only convenience sync.

---

## Date States

| State | Description | Customer Sees |
|-------|-------------|---------------|
| `available` | No confirmed booking, not blocked | Selectable / Green |
| `booked` | Has a confirmed booking | Unselectable / Red/Grey |
| `blocked` | Admin-blocked manually | Unselectable / Red/Grey |

---

## Django Models

### BlockedDate

```python
class BlockedDate(models.Model):
    date = models.DateField(unique=True)
    reason = models.CharField(max_length=255, blank=True)  # Admin-only note
    blocked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Blocked: {self.date} ({self.reason or 'No reason'})"
```

### TimeSlot (referenced in 07-booking-management.md)

```python
class TimeSlot(models.Model):
    label = models.CharField(max_length=50)
    start_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
```

---

## Availability Logic

```python
# bookings/availability.py

from datetime import date, timedelta
from .models import Booking, BlockedDate

def get_date_status(check_date: date) -> str:
    """
    Returns 'available', 'booked', or 'blocked' for a given date.
    """
    if BlockedDate.objects.filter(date=check_date).exists():
        return 'blocked'

    if Booking.objects.filter(
        booking_date=check_date,
        status=Booking.Status.CONFIRMED
    ).exists():
        return 'booked'

    return 'available'


def get_available_dates(start_date: date, end_date: date) -> dict:
    """
    Returns a dict mapping each date in range to its status.
    Used to render the customer-facing calendar.
    """
    result = {}
    current = start_date
    while current <= end_date:
        result[current] = get_date_status(current)
        current += timedelta(days=1)
    return result


def is_date_available(check_date: date) -> bool:
    return get_date_status(check_date) == 'available'
```

---

## Customer-Facing Calendar

- Displays a monthly calendar
- Dates are loaded from the backend via an API endpoint or HTMX partial
- Visual encoding:
  - **Green** or **White with border**: Available (selectable)
  - **Grey with strikethrough** or **Red tint**: Booked or Blocked (not selectable)
  - **Today's date**: Highlighted
  - **Past dates**: Always unselectable
- Minimum advance booking: 0 days (same-day) or 1 day — to be confirmed by client
- Maximum advance booking: 90 days by default (configurable)

### Calendar API Endpoint

```
GET /api/availability/?month=2026-02
Response: {
  "2026-02-01": "available",
  "2026-02-02": "booked",
  "2026-02-03": "blocked",
  ...
}
```

---

## Admin Calendar View

- Full monthly calendar at `/admin/calendar/`
- All three states visible (available, booked, blocked)
- Booked dates: click to see booking reference and customer summary
- Available dates: click to block
- Blocked dates: click to unblock
- Navigation: previous/next month

---

## Time Slot Availability

- A time slot on a given date is only selectable if the date itself is `available`
- Since only one booking per day is allowed, once any confirmed booking exists for a date, all time slots are locked
- Time slots are admin-configured globally (same slots every available day in MVP)

---

## Concurrency / Race Conditions

When two customers attempt to book the same date simultaneously:
1. Both create a `DRAFT` booking.
2. The first to successfully complete Stripe payment has their booking confirmed.
3. When the second Stripe webhook arrives, the system checks if the date is still available.
4. If the date is now booked: cancel the second booking, refund the payment via Stripe, and notify the customer.

> Implementation note: Use database-level uniqueness or a locking mechanism to prevent double-booking.

### Recommended approach:
```python
# In the webhook handler:
from django.db import transaction

with transaction.atomic():
    if not is_date_available(booking.booking_date):
        # Initiate Stripe refund
        # Set booking status to cancelled
        # Send cancellation email
        return
    booking.status = Booking.Status.CONFIRMED
    booking.save()
```

---

## Future Phase Considerations

> **Google Calendar Phase 2**
>
> The Booking model already includes `google_calendar_event_id` (see `07-booking-management.md`).
> When Phase 2 is implemented:
> - Confirmed bookings will be synced to Google Calendar as events.
> - The application database remains the source of truth.
> - Google Calendar is a display/notification convenience only.
> - If the Google Calendar sync fails, the booking remains confirmed in the database.
> - See `10-google-calendar.md` for the full Phase 2 specification.

---

## Related Documents
- `07-booking-management.md`
- `10-google-calendar.md` (Phase 2)
- `16-api-and-backend-architecture.md`
