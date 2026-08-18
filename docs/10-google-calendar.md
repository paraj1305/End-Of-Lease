# 10 — Google Calendar Integration

> # ⚠️ PHASE 2 / FUTURE FEATURE — NOT PART OF MVP
>
> Google Calendar integration is **explicitly excluded from the initial MVP**.
> **Do NOT implement any Google Calendar code during Phase 1 development.**
>
> This document serves as a specification for Phase 2 implementation only.
>
> The application's own database is — and will always remain — the **source of truth** for all bookings and availability.

---

## Why Phase 2?

Google Calendar integration was identified in the original client requirements but has been deliberately deferred to avoid:
- Added OAuth 2.0 complexity in the MVP
- Google API authentication setup overhead
- Risk of booking system dependency on third-party service availability
- Additional development time that delays the MVP launch

The MVP booking system works completely independently of Google Calendar.

---

## MVP Architecture Decision

The booking system is designed so that Google Calendar can be added later **without any database migrations or architectural changes**:

1. The `Booking` model already includes a `google_calendar_event_id` field (blank, unused in MVP).
2. The booking status lifecycle is fully self-contained.
3. Availability is determined entirely from the application database.
4. Google Calendar, when added in Phase 2, will be a **one-way push sync** — confirmed bookings are sent to Google Calendar as events.
5. Google Calendar will never be used as an availability source — the application database is always authoritative.

---

## Phase 2 Requirements (Specification)

### Purpose
Allow the business owner/admin to see confirmed appointments on their personal/business Google Calendar on mobile and other devices.

### Integration Type
- **One-way push sync**: Application → Google Calendar
- Triggered when a booking status changes to `CONFIRMED`
- Optionally triggered when a booking is cancelled (delete event from calendar)

### Data Synced
Each Google Calendar event should include:
- **Event title:** e.g., "Cleaning — John Smith (EOL-2026-00042)"
- **Date and time:** booking date + time slot
- **Duration:** estimated (to be confirmed — e.g., 3 hours default per package)
- **Description:**
  - Customer name, phone, email
  - Service address
  - Package name
  - Add-ons selected
  - Deposit paid
  - Remaining amount
  - Booking reference
- **Location:** Service address

### Technical Approach (Phase 2)

#### Prerequisites
- Google Cloud Project with Google Calendar API enabled
- OAuth 2.0 credentials (client ID + secret)
- Service Account OR OAuth refresh token stored securely

#### Required Libraries
```
google-auth
google-auth-oauthlib
google-api-python-client
```

#### Admin OAuth Setup Flow
1. Admin navigates to admin settings → Google Calendar
2. Clicks "Connect Google Calendar"
3. OAuth consent flow (Google login + permission grant)
4. Refresh token stored securely in environment variables or database (encrypted)
5. Calendar ID configured (which calendar to sync to)

#### Sync Logic (Phase 2)

```python
# Future: bookings/services/google_calendar.py

def create_calendar_event(booking):
    """
    Creates a Google Calendar event for a confirmed booking.
    Called asynchronously after booking confirmation.
    
    Args:
        booking: Booking instance with status=CONFIRMED
    
    Returns:
        str: Google Calendar event ID (stored in booking.google_calendar_event_id)
    
    NOTE: This function must NEVER be called in MVP. Phase 2 only.
    """
    pass

def delete_calendar_event(booking):
    """
    Deletes the Google Calendar event for a cancelled booking.
    Phase 2 only.
    """
    pass
```

#### Error Handling (Phase 2)
- If Google Calendar sync fails, the booking remains `CONFIRMED` — do NOT roll back.
- Log the sync failure.
- Admin can manually retry sync from the admin panel.
- Sync failures must NOT affect the customer experience.

### Database Field (Already Present in MVP)

The `Booking` model already includes:
```python
google_calendar_event_id = models.CharField(max_length=255, blank=True)
```

This field is blank/unused in MVP. In Phase 2, it stores the Google Calendar event ID for update/delete operations.

---

## Phase 2 Admin UI

- Google Calendar settings section in admin settings page
- Connect / Disconnect Google Calendar button
- Sync status for each booking (synced / not synced / failed)
- Manual sync button per booking
- Bulk sync option

---

## What is NOT in Scope (Even in Phase 2)

- Two-way sync (Google Calendar → Application)
- Reading availability from Google Calendar
- Allowing customers to add events to their own Google Calendar (may be considered separately)
- Multiple calendar support

---

## Related Documents
- `07-booking-management.md` — `google_calendar_event_id` field
- `22-development-phases.md` — Phase 2 timeline
- `24-future-enhancements.md` — Other future features
