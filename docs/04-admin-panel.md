# 04 — Admin Panel

## Overview
The admin panel is a secured web interface for the business owner/admin to manage all aspects of the platform. It uses Django's admin framework as a foundation, extended with custom views and a calendar interface.

---

## Access & Security

- Admin panel accessible at `/admin/`
- Secured by Django's authentication system (username + password)
- HTTPS required
- Session timeout after inactivity
- Admin users created via Django `createsuperuser` command or via the admin interface

---

## Admin Dashboard

**URL:** `/admin/`

**Widgets / Sections:**
| Widget | Description |
|--------|-------------|
| Today's Bookings | Count and list of today's appointments |
| Upcoming Bookings | Next 7 days summary |
| Total Confirmed Bookings | All-time count |
| Pending Draft Bookings | Bookings awaiting payment |
| Recent Bookings | Latest 10 bookings with status |
| Revenue Summary | Deposit collected (current month / all-time) |
| Quick Actions | Block a date / Add package / Add add-on |

---

## Booking Management

**URL:** `/admin/bookings/`

### Bookings List View
- Columns: Ref #, Customer Name, Package, Date, Time, Status, Deposit Paid, Created At
- Filters: Status, Date range, Payment status
- Search: Customer name, email, booking reference

### Booking Detail View
- All booking details (package, add-ons, date, time, customer info)
- Payment status and amount
- Booking reference
- Ability to change status: Confirmed / Cancelled / Completed
- Notes field (internal use)

### Booking Status Flow
```
Draft → Confirmed (on payment) → Completed (after cleaning) or Cancelled
```

---

## Package Management

**URL:** `/admin/packages/`

### Package List View
- Columns: Name, Area, Price, Status, Display Order
- Toggle active/inactive
- Reorder packages

### Package Create / Edit Form
| Field | Type | Required |
|-------|------|----------|
| Name | CharField | Yes |
| Approximate Area | CharField | Yes |
| Base Price | DecimalField | Yes |
| Short Description | TextField | Yes |
| Long Description | TextField | No |
| Included Services | TextField / JSON | Yes |
| Active | BooleanField | Yes |
| Display Order | IntegerField | Yes |

---

## Add-on Management

**URL:** `/admin/addons/`

### Add-on List View
- Columns: Name, Price, Status, Display Order
- Toggle active/inactive

### Add-on Create / Edit Form
| Field | Type | Required |
|-------|------|----------|
| Name | CharField | Yes |
| Short Description | TextField | Yes |
| Price | DecimalField | Yes |
| Active | BooleanField | Yes |
| Display Order | IntegerField | Yes |

---

## Availability & Calendar Management

**URL:** `/admin/calendar/`

### Admin Calendar View
- Monthly calendar view
- Colour-coded dates:
  - 🟢 Available: No booking, not blocked
  - 🔴 Booked: Has a confirmed booking
  - 🔵 Blocked: Manually blocked by admin
- Clicking a Booked date: shows booking summary and link to full details
- Clicking an Available date: option to Block
- Clicking a Blocked date: option to Unblock

### Date Block/Unblock
- Admin selects a date → clicks "Block Date" → date becomes unavailable for customers
- Admin selects a blocked date → clicks "Unblock" → date becomes available again
- Optionally: Admin can add a reason/note for blocking (internal only)

### Time Slot Management
**URL:** `/admin/timeslots/`
- Admin can add, edit, remove time slots (e.g., 8:00 AM, 9:00 AM, 10:00 AM, etc.)
- Time slots are global (same each day unless overridden — Phase 2)

---

## Settings

**URL:** `/admin/settings/`

| Setting | Description |
|---------|-------------|
| Business Name | For emails and confirmation pages |
| Contact Email | Admin email for notifications |
| Contact Phone | For display on confirmation page |
| Deposit Percentage | Default: 10 (must be confirmed by client) |
| SMTP Settings | For outgoing emails |
| Stripe Public Key | Stripe publishable key |
| Stripe Secret Key | Stripe secret key (stored securely) |

---

## Google Calendar (PHASE 2 ONLY)

> ⚠️ **NOT implemented in MVP.**
> Google Calendar integration is planned for Phase 2.
> See `10-google-calendar.md` for future integration specification.

---

## Admin Navigation Structure

```
Admin Dashboard
├── Bookings
│   ├── All Bookings
│   └── Draft Bookings
├── Packages
│   ├── Manage Packages
│   └── Add Package
├── Add-ons
│   ├── Manage Add-ons
│   └── Add Add-on
├── Availability
│   ├── Calendar View
│   ├── Block/Unblock Dates
│   └── Time Slots
├── Settings
│   └── General Settings
└── [Phase 2] Google Calendar
```

---

## Related Documents
- `05-packages.md`
- `06-addons.md`
- `07-booking-management.md`
- `08-availability-and-calendar.md`
- `10-google-calendar.md` (Phase 2)
