# 03 — User Booking Flow

## Overview
This document defines the complete step-by-step customer booking journey. The flow must work without any customer account. Every step should feel simple, fast, and trustworthy.

**Guiding principle:** A customer should be able to complete a booking in under 3 minutes on mobile.

---

## Flow Diagram

```
Landing Page
    │
    ▼
[BOOK A CLEANING] CTA (Hero / Sticky / Any section)
    │
    ▼
Step 1: Select Package
    │
    ▼
Step 2: Select Add-ons (optional)
    │
    ▼
Step 3: Select Date & Time
    │
    ▼
Step 4: Enter Customer Details
    │
    ▼
Step 5: Review Booking Summary
    │
    ▼
Step 6: Pay 10% Deposit (Stripe)
    │
    ├── Payment Failed → Show error → Allow retry
    │
    └── Payment Successful
            │
            ▼
        Step 7: Booking Confirmation
            │
            ▼
        Email Confirmation sent to customer
```

---

## Detailed Steps

### Step 1 — Select Cleaning Package

**Page / Component:** Package selection screen

**What the customer sees:**
- List of active cleaning packages as cards
- Each card shows: package name, approximate area/sqft, starting price, short description, "What's Included" (expandable or visible), a "Select" / "Book Now" button
- Packages are loaded dynamically from the database

**Business rules:**
- Only active packages are displayed
- Packages are ordered by display_order field
- Selecting a package proceeds to Step 2

---

### Step 2 — Select Add-on Services (Optional)

**Page / Component:** Add-on selection screen

**What the customer sees:**
- List of active add-on services as cards
- Each card: name, short description, price (e.g., "+ $20")
- Customer can select zero or more add-ons (checkboxes or toggle cards)
- Running total updates as add-ons are toggled
- "Continue" button to proceed

**Business rules:**
- Only active add-ons are displayed
- Add-on prices are loaded from the database
- Customer can skip this step (zero add-ons selected is valid)

---

### Step 3 — Select Date & Time

**Page / Component:** Date/time picker

**What the customer sees:**
- Calendar view (monthly) with colour-coded dates:
  - 🟢 Green/White: Available
  - 🔴 Red/Grey: Booked or Blocked (unselectable)
- Customer selects an available date
- Available time slots appear for the selected date
- Customer selects a time slot
- "Continue" button to proceed

**Business rules:**
- Only one booking is allowed per day
- Booked dates (confirmed payment exists) are unavailable
- Blocked dates (admin-blocked) are unavailable
- Time slots are configured by admin
- The calendar must update in real-time (HTMX or JS fetch)

---

### Step 4 — Enter Customer Details

**Page / Component:** Customer details form

**Required fields:**
| Field | Type | Validation |
|-------|------|-----------|
| Full Name | Text | Required, min 2 chars |
| Phone Number | Tel | Required, AU format |
| Email Address | Email | Required, valid format |
| Service Address — Street | Text | Required |
| Service Address — Suburb | Text | Required |
| Service Address — Postcode | Text | Required, 4-digit AU postcode |
| Service Address — State | Select | Required (NSW, VIC, QLD, etc.) |

**Optional fields:**
| Field | Type |
|-------|------|
| Special Instructions / Notes | Textarea |

**Business rules:**
- All required fields must be validated client-side and server-side
- No account is created for the customer
- Data is temporarily stored in the session until payment succeeds

---

### Step 5 — Review Booking Summary

**Page / Component:** Summary/review screen

**What the customer sees:**
| Item | Value |
|------|-------|
| Package | e.g., 3 BHK End of Lease Cleaning |
| Package Price | e.g., $350.00 |
| Add-ons (if any) | e.g., Garden Cleaning +$30.00 |
| Subtotal | e.g., $380.00 |
| Deposit (10%) | e.g., $38.00 ← Pay today |
| Remaining amount | e.g., $342.00 ← Pay on day |
| Date | e.g., Saturday, 25 January 2026 |
| Time | e.g., 9:00 AM |
| Address | e.g., 12 Main St, Parramatta NSW 2150 |
| Name | e.g., John Smith |
| Email | e.g., john@email.com |
| Phone | e.g., 0412 345 678 |

**Edit links:** Allow the customer to go back and edit each section.

**CTA:** "Proceed to Payment" (large, prominent button)

---

### Step 6 — Payment (Stripe)

**Page / Component:** Stripe Checkout or Stripe Elements embedded form

**What the customer sees:**
- Clear statement: "You are paying a 10% deposit of $XX.XX today"
- Stripe payment form (card number, expiry, CVV)
- Total deposit amount clearly displayed
- "Pay $XX.XX Now" button
- Security badge / trust signals

**Business rules:**
- A Stripe PaymentIntent is created server-side before the payment form loads
- The exact deposit amount (10% of package + add-ons) is calculated server-side
- A provisional/draft Booking record is created in the database before payment
- On payment success webhook: booking status is updated to Confirmed, date is marked as Booked
- On payment failure: provisional booking remains in Draft state; customer may retry
- Draft bookings older than 30 minutes that never completed payment should be periodically cleaned up (management command)

---

### Step 7 — Booking Confirmation

**Page / Component:** Confirmation page

**What the customer sees:**
- ✅ Success message: "Your booking is confirmed!"
- Booking reference number (unique, human-readable, e.g., EOL-2026-00042)
- Summary of all booking details
- Amount paid today
- Remaining amount (and note that this will be collected on the cleaning day)
- Business contact information
- "Return to Home" / "View another service" buttons

**Email sent to customer:**
- Same information as the confirmation page
- Formatted, branded HTML email
- Subject: "Your Cleaning Booking is Confirmed — Ref: EOL-2026-00042"

---

## Booking Session Management

| State | Description |
|-------|-------------|
| `in_progress` | Customer is actively completing the booking flow |
| `draft` | Customer has started payment; payment not yet confirmed |
| `confirmed` | Stripe payment succeeded; booking is locked in |
| `cancelled` | Admin-cancelled or auto-cancelled (e.g., after extended draft period) |
| `completed` | Cleaning job has been completed |

Session data held temporarily:
- Selected package ID
- Selected add-on IDs
- Selected date and time slot
- Customer details

Session data is cleared after a confirmed booking record is created.

---

## Mobile-Specific Considerations

- Sticky **BOOK A CLEANING** button at bottom of screen on landing page
- All form steps must work on a 375px screen without horizontal scroll
- Date picker must use a mobile-friendly calendar widget (not browser default `<input type="date">` alone — provide a styled calendar)
- Large touch targets (minimum 44×44px)
- Number inputs with appropriate keyboard types (`tel`, `email`, `number`)
- Autofill support for name, email, phone, address

---

## Accessibility

- All form fields have associated `<label>` elements
- Error messages are associated via `aria-describedby`
- Focus states visible on all interactive elements
- Keyboard navigation works through all steps
- Color is not the only means of communicating date status (use icons or text labels too)

---

## Related Documents
- `02-functional-requirements.md` — FR-02 Booking Flow
- `05-packages.md` — Package model
- `06-addons.md` — Add-on model
- `08-availability-and-calendar.md` — Availability logic
- `09-payments.md` — Stripe payment integration
- `14-email-notifications.md` — Email confirmation
