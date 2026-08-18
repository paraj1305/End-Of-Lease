# 23 — Acceptance Criteria

## Overview
This document defines the conditions that must be satisfied for the MVP to be considered complete and ready for client handover.

---

## AC-01: Landing Page

- [ ] Landing page loads in under 3 seconds on a mobile device (LTE connection)
- [ ] Hero section displays a video (or poster image fallback) with a transformation concept
- [ ] Scroll-driven video interaction works on desktop and degrades gracefully on mobile
- [ ] Reduced-motion preference disables scroll animation and shows a static or auto-play version
- [ ] All 12 sections are present (Hero, Trust, How It Works, Packages, Add-ons, Before/After, Why Us, Reviews, Areas, FAQ, CTA, Footer)
- [ ] Every major section CTA leads to the booking flow
- [ ] Sticky "Book a Cleaning" CTA is visible on mobile after hero scrolls out of view
- [ ] Landing page is mobile-first and fully usable at 375px width without horizontal scroll
- [ ] Package cards are loaded dynamically from the admin database — no hardcoded prices
- [ ] Add-on cards are loaded dynamically from the admin database

---

## AC-02: Booking Flow

- [ ] Customer can complete a full booking without creating an account
- [ ] Booking flow has 5 clear steps with progress indication
- [ ] Package selection shows only active packages
- [ ] Add-on selection shows only active add-ons
- [ ] Running total updates correctly as add-ons are selected/deselected
- [ ] Calendar shows available, booked, and blocked dates correctly
- [ ] Booked dates (confirmed booking) are unselectable
- [ ] Blocked dates (admin-blocked) are unselectable
- [ ] Time slots are displayed and selectable for available dates
- [ ] Customer details form validates all required fields client-side and server-side
- [ ] Booking review shows correct summary including deposit amount (10%)
- [ ] Stripe payment form loads correctly
- [ ] Successful payment (test card 4242) confirms the booking
- [ ] Confirmation page shows booking reference, all details, deposit paid, remaining amount
- [ ] Confirmation email is sent to the customer within 1 minute of payment
- [ ] Date is no longer available to other customers after booking is confirmed

---

## AC-03: Packages & Add-ons

- [ ] Admin can create, edit, activate, deactivate packages from admin panel
- [ ] Inactive packages are not visible to customers
- [ ] Admin can create, edit, activate, deactivate add-ons from admin panel
- [ ] Inactive add-ons are not visible to customers
- [ ] Price changes in admin immediately affect new bookings
- [ ] Existing confirmed bookings retain their original price

---

## AC-04: Admin Calendar & Availability

- [ ] Admin calendar shows monthly view with correct date states
- [ ] Admin can block an available date
- [ ] Blocked date is immediately unavailable to customers
- [ ] Admin can unblock a blocked date
- [ ] Admin can view booking details by clicking a booked date
- [ ] One booking per day rule is enforced

---

## AC-05: Admin Dashboard & Bookings

- [ ] Admin dashboard shows booking overview metrics
- [ ] Admin can view all bookings with filtering and search
- [ ] Admin can view full details of any booking
- [ ] Admin can update booking status (Confirmed/Cancelled/Completed)
- [ ] Admin can view payment status for each booking

---

## AC-06: PWA

- [ ] Web App Manifest is present and valid
- [ ] Service Worker is registered
- [ ] Offline fallback page is shown when offline
- [ ] Website can be installed as a PWA on Android Chrome
- [ ] Website can be added to home screen on iOS Safari
- [ ] Lighthouse PWA audit passes all checks

---

## AC-07: SEO

- [ ] All 5 public pages have unique `<title>` tags
- [ ] All 5 public pages have unique `<meta name="description">` tags
- [ ] Each page has exactly one `<h1>`
- [ ] LocalBusiness JSON-LD schema is present on all pages
- [ ] FAQ schema is present on the FAQ section
- [ ] Open Graph tags are present
- [ ] `/sitemap.xml` is accessible and includes all public pages
- [ ] `/robots.txt` is accessible and correctly configured
- [ ] All images have descriptive alt text
- [ ] No important content exists only inside video (all text is in HTML)

---

## AC-08: Performance

- [ ] Lighthouse Performance score ≥ 85 on mobile
- [ ] Lighthouse Accessibility score ≥ 90
- [ ] Lighthouse SEO score ≥ 90
- [ ] LCP < 3.0 seconds on mobile (target < 2.5s)
- [ ] CLS < 0.1
- [ ] Hero video has a poster image (no blank loading flash)

---

## AC-09: Payment & Security

- [ ] Stripe keys are stored in environment variables, not in code
- [ ] Stripe webhook verifies signature before processing
- [ ] CSRF protection active on all POST views
- [ ] HTTPS enforced in production
- [ ] No sensitive customer data is logged

---

## AC-10: Google Calendar

- [ ] ✅ Google Calendar is NOT implemented in MVP
- [ ] The `google_calendar_event_id` field exists in the Booking model (unused)
- [ ] A placeholder `google_calendar.py` service file exists with no implementation
- [ ] No Google API credentials are required to run the MVP

---

## AC-11: Browser & Device Compatibility

- [ ] Booking flow works correctly on iPhone Safari (iOS 15+)
- [ ] Booking flow works correctly on Android Chrome
- [ ] Landing page renders correctly on Chrome Desktop, Safari Desktop, Firefox Desktop
- [ ] No horizontal scrolling on mobile at any point in the booking flow or landing page

---

## Handover Checklist

Before delivering to client:
- [ ] All placeholder content replaced with client content (or clearly noted as pending)
- [ ] Live Stripe keys configured (not test keys)
- [ ] Admin superuser created for client
- [ ] Client briefed on admin panel usage
- [ ] DNS and HTTPS configured for production domain
- [ ] Stripe webhook URL updated in Stripe Dashboard to production URL
- [ ] Email SMTP configured and tested in production
- [ ] Google Analytics / Tag Manager installed (if requested)
