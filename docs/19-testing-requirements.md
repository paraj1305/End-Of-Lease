# 19 — Testing Requirements

## Overview
This document defines the testing strategy, test cases, and quality assurance requirements for the MVP.

---

## Testing Philosophy
- Test business logic thoroughly (pricing, availability, booking status)
- Test the critical path (booking flow + payment) end-to-end
- Ensure mobile devices and key browsers are tested before launch
- Automated tests for core logic; manual testing for UI/UX

---

## Test Categories

### 1. Unit Tests (Django)
**Location:** `apps/bookings/tests/`

#### Pricing Logic
- [ ] Deposit is exactly 10% of (package + add-ons)
- [ ] Zero add-ons: deposit = 10% of package only
- [ ] Deposit rounds correctly to 2 decimal places
- [ ] Remaining amount = subtotal - deposit

#### Availability Logic
- [ ] Available date returns `available`
- [ ] Date with confirmed booking returns `booked`
- [ ] Blocked date returns `blocked`
- [ ] Draft booking does NOT affect date status
- [ ] Cancelled booking frees up the date

#### Booking Reference Generation
- [ ] Reference is unique
- [ ] Reference follows expected format (EOL-YYYY-XXXXXX)

#### Draft Booking Cleanup
- [ ] Draft bookings older than 30 minutes are removed
- [ ] Confirmed bookings are not removed
- [ ] Recent draft bookings (< 30 min) are not removed

### 2. Integration Tests

#### Booking Flow
- [ ] Complete booking flow stores data correctly in session at each step
- [ ] Navigating back preserves previous step data
- [ ] Booking creation from session data creates correct Booking record

#### Stripe Webhook
- [ ] Valid webhook with correct signature → processes successfully
- [ ] Invalid signature → returns 400
- [ ] `payment_intent.succeeded` → booking confirmed, email sent
- [ ] `payment_intent.succeeded` on booked date → refund initiated, booking cancelled

#### Admin Operations
- [ ] Admin can block a date
- [ ] Blocked date is not available to customers
- [ ] Admin can unblock a date
- [ ] Unblocked date becomes available again

### 3. End-to-End Tests (Manual)

#### Customer Booking Flow
- [ ] Open landing page → hero video loads
- [ ] Click "Book a Cleaning" → goes to package selection
- [ ] Select a package → proceed to add-ons
- [ ] Select add-ons → running total updates correctly
- [ ] Select available date → time slots appear
- [ ] Select time slot → proceed to customer details
- [ ] Fill in customer details → proceed to review
- [ ] Review shows correct summary
- [ ] Pay deposit with test card 4242 4242 4242 4242
- [ ] Confirmation page appears with booking reference
- [ ] Confirmation email received

#### Mobile Booking Flow
- [ ] Complete above flow on iPhone Safari (375px)
- [ ] Complete above flow on Android Chrome
- [ ] Sticky CTA visible and functional on mobile
- [ ] Calendar is usable on touch devices
- [ ] Form inputs do not cause horizontal scroll

#### Admin Operations
- [ ] Login to admin
- [ ] View booking list
- [ ] View booking details
- [ ] Block a date → verify customer cannot book it
- [ ] Unblock the date → verify customer can book it
- [ ] Create a new package
- [ ] Deactivate a package → verify it's hidden from customers
- [ ] Add an add-on → verify it appears in booking flow

### 4. Browser/Device Compatibility Testing

| Browser | Platform | Priority |
|---------|---------|---------|
| Chrome (latest) | Desktop | High |
| Safari (latest) | Mac | High |
| Safari (iOS 15+) | iPhone | HIGH |
| Chrome (Android 10+) | Android | HIGH |
| Firefox (latest) | Desktop | Medium |
| Edge (latest) | Desktop | Medium |
| Samsung Internet | Android | Low |

### 5. Performance Testing (Lighthouse)

Run Lighthouse audit on:
- [ ] Landing page (mobile) → target ≥ 90 score
- [ ] Booking step 1 (mobile)
- [ ] Confirmation page (mobile)

Targets:
- Performance ≥ 90
- Accessibility ≥ 90
- Best Practices ≥ 90
- SEO ≥ 90
- PWA: passes all checks

### 6. Payment Testing (Stripe Test Mode)

| Test Scenario | Card Number | Expected Result |
|--------------|-------------|----------------|
| Successful payment | 4242 4242 4242 4242 | Booking confirmed |
| Card declined | 4000 0000 0000 0002 | Error shown, can retry |
| 3D Secure | 4000 0025 0000 3155 | 3DS challenge, then confirm |
| Insufficient funds | 4000 0000 0000 9995 | Decline message |

### 7. Accessibility Testing

- [ ] All images have alt text
- [ ] All form fields have labels
- [ ] Keyboard navigation works through booking flow
- [ ] Screen reader can follow booking steps
- [ ] Color contrast meets WCAG AA (4.5:1 for text)
- [ ] Focus states are visible
- [ ] `prefers-reduced-motion` stops/reduces animations

---

## Testing Environment

### Local Development
```bash
python manage.py test apps/
```

### Stripe Test Mode
Use Stripe test keys (`pk_test_...` / `sk_test_...`) in development.
Use Stripe CLI to forward webhooks locally:
```bash
stripe listen --forward-to localhost:8000/webhooks/stripe/
```

---

## Related Documents
- `09-payments.md`
- `08-availability-and-calendar.md`
- `11-pwa-requirements.md`
