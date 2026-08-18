# 02 — Functional Requirements

## Overview
This document defines all functional requirements for the End of Lease Cleaning platform MVP.

---

## FR-01: Landing Page

### FR-01.1 Hero Section
- Display a full-screen/large video hero with a cleaning transformation theme (dirty → clean).
- Support scroll-driven video progression (see `27-landing-page-design-system.md`).
- Display a primary headline and supporting subheading (configurable from admin or template).
- Primary CTA: **BOOK A CLEANING** (links to booking flow).
- Secondary CTA: **VIEW SERVICES** (links to packages section or services page).
- Fallback for reduced-motion / low-bandwidth: autoplay muted looped video or static before/after image.

### FR-01.2 Trust / Value Proposition Section
- Display 4–6 trust signal icons/cards (e.g., Professional Cleaners, Easy Booking, Reliable Service, Transparent Pricing).
- Content should be manageable from admin (Phase 2); static for MVP.

### FR-01.3 How It Works (Simple Booking Steps)
- Display numbered steps showing how easy booking is (5-step process).
- Steps: Choose Home → Select Add-ons → Choose Date & Time → Pay Deposit → We Clean.

### FR-01.4 Cleaning Packages Section
- Display active cleaning packages from the database.
- Each card: package name, approx. area, starting price, short description, included items, BOOK NOW button.
- Data must come dynamically from Django admin — no hardcoded prices.

### FR-01.5 Add-on Services Section
- Display active add-on services from the database.
- Each card: name, description, price, Add button.
- Data must come dynamically from Django admin.

### FR-01.6 Before / After Section
- Display a visual before/after slider or scroll animation.
- Must be performance-optimised (image-based preferred over video for this section).
- Use placeholder images until client provides licensed photos.

### FR-01.7 Why Choose Us Section
- Display 4–6 key benefits/differentiators.
- Static content for MVP; admin-manageable in Phase 2.

### FR-01.8 Testimonials Section
- Display customer testimonials.
- For MVP: clearly marked placeholder content — do NOT use fabricated real reviews.
- Phase 2: admin-manageable testimonials.

### FR-01.9 Service Areas Section
- Display SEO-friendly list of suburbs/cities served.
- Content: placeholder/admin-defined; client must provide final list.
- Structure must support easy expansion.

### FR-01.10 FAQ Section
- Display frequently asked questions and answers.
- Covers: what's included, how booking works, deposit policy, cancellation, supplies, cleaning duration.
- Static for MVP; admin-manageable in Phase 2.

### FR-01.11 Final CTA Section
- Strong closing CTA: "Ready for a Cleaner Home?" + **BOOK YOUR CLEANING** button.

### FR-01.12 Footer
- Logo, navigation links, services, contact info, service areas, Privacy Policy, Terms, Cancellation Policy, social links.

### FR-01.13 Sticky Mobile CTA
- On mobile screens, display a sticky **BOOK A CLEANING** button at the bottom of the viewport.
- Must not obscure footer content.

---

## FR-02: Booking Flow

### FR-02.1 Package Selection
- Customer selects a cleaning package from the list of active packages.
- Display: name, area, price, included services.
- No account required.

### FR-02.2 Add-on Selection
- Customer can optionally select one or more add-on services.
- Display: name, description, price.
- Running total updates dynamically (HTMX or JS).

### FR-02.3 Date & Time Selection
- Display a calendar view showing:
  - Available dates (can book)
  - Booked dates (cannot book — greyed out)
  - Blocked dates (cannot book — greyed out)
- Only one booking per day is allowed.
- Display available time slots for the selected date.
- Time slots are admin-configured.

### FR-02.4 Customer Details Form
- Fields (required):
  - Full name
  - Phone number
  - Email address
  - Service address (street, suburb, postcode, state)
- Optional fields (to be confirmed by client):
  - Special instructions / notes

### FR-02.5 Booking Summary & Review
- Show full summary before payment:
  - Package name and price
  - Selected add-ons and prices
  - Date and time
  - Customer details
  - Subtotal
  - Deposit amount (10%)
  - Remaining amount (to be paid on day)

### FR-02.6 Payment (Stripe)
- Customer pays 10% deposit via Stripe Checkout or Stripe Elements.
- Booking is confirmed only after successful payment.
- Display clear deposit amount and remaining balance.
- Support cards (credit/debit).
- Country: Australia (AUD — to be confirmed).

### FR-02.7 Booking Confirmation
- After successful payment, display confirmation page with:
  - Unique booking reference number
  - Package name
  - Add-ons
  - Date and time
  - Service address
  - Amount paid (deposit)
  - Remaining amount
  - Business contact info
- Send confirmation email to customer with all details.

---

## FR-03: Cleaning Packages

### FR-03.1 Package Model
Each package must have:
- Name (e.g., "2 BHK", "3 BHK")
- Approximate area / square footage range
- Base price
- Short description (for landing page cards)
- Detailed description (for services page)
- List of included services / cleaning items
- Active/Inactive status
- Display order (for sorting)

### FR-03.2 Admin Management
- Admin can create, edit, delete, activate, deactivate packages.
- Price changes take effect immediately for new bookings.
- Inactive packages are hidden from the customer-facing site.

---

## FR-04: Add-on Services

### FR-04.1 Add-on Model
Each add-on must have:
- Name (e.g., "Garden Cleaning")
- Short description
- Additional price
- Active/Inactive status
- Display order

### FR-04.2 Admin Management
- Admin can create, edit, delete, activate, deactivate add-ons.
- Price changes take effect immediately for new bookings.
- Inactive add-ons are hidden from customers.

---

## FR-05: Availability & Calendar

### FR-05.1 Booking Dates
- Each date can have one of three states: Available, Booked, Blocked.
- A date becomes Booked automatically when a confirmed booking exists.
- Admin can set a date to Blocked manually.

### FR-05.2 Time Slots
- Time slots are admin-configurable (e.g., 8:00 AM, 10:00 AM, 12:00 PM, 2:00 PM).
- A time slot is available only if the date itself is available.
- Since only one booking is allowed per day, once any time slot is booked, all slots on that date become unavailable.

### FR-05.3 Admin Calendar View
- Admin sees a monthly calendar with colour-coded dates.
- Clicking a booked date shows booking details.
- Admin can block/unblock dates.

---

## FR-06: Admin Panel

### FR-06.1 Dashboard
- Overview widgets: total bookings, today's bookings, pending payments, upcoming appointments.

### FR-06.2 Bookings Management
- View all bookings (searchable, filterable by date/status).
- View individual booking details.
- Update booking status (Confirmed, Cancelled, Completed).
- View payment status.

### FR-06.3 Package Management
- Full CRUD for cleaning packages.

### FR-06.4 Add-on Management
- Full CRUD for add-on services.

### FR-06.5 Availability Management
- View/edit time slots.
- Block/unblock dates.
- View the admin calendar.

### FR-06.6 Settings
- Business name, contact details, email settings.
- Deposit percentage (default 10%).

---

## FR-07: PWA

- Web App Manifest with app name, icons, theme color.
- Service Worker for offline support (at minimum: offline fallback page).
- Installable on iOS and Android home screens.
- Fast-loading (Core Web Vitals targets).

---

## FR-08: SEO

- Each public page has a unique `<title>` and `<meta description>`.
- Proper H1/H2/H3 hierarchy.
- Semantic HTML5 elements.
- LocalBusiness schema (JSON-LD).
- Service schema.
- FAQ schema (on FAQ sections).
- Open Graph metadata for social sharing.
- Canonical URLs.
- XML sitemap at `/sitemap.xml`.
- `robots.txt` at `/robots.txt`.
- Image alt text on all images.
- All important content in crawlable HTML (not locked inside video).

---

## FR-09: Email Notifications

### FR-09.1 Customer Booking Confirmation
- Sent automatically after successful payment.
- Contains: booking reference, package, add-ons, date, time, address, deposit paid, remaining amount.

### FR-09.2 Admin Notification (Optional for MVP)
- New booking notification to admin email.

---

## FR-10: Performance

- Hero video: compressed, web-optimised (WebM/MP4), with poster image.
- Lazy loading for below-the-fold images.
- WebP/AVIF image formats where supported.
- Minimal blocking JavaScript.
- Django server-side rendering for fast initial load.
- Target: Good Core Web Vitals (LCP < 2.5s, FID/INP < 200ms, CLS < 0.1).

---

## Non-Functional Requirements

| Requirement | Specification |
|-------------|--------------|
| Availability | 99%+ uptime in production |
| Security | HTTPS, CSRF protection, input validation, Stripe secure payment |
| Accessibility | WCAG 2.1 AA target, `prefers-reduced-motion` support |
| Browser support | Chrome, Safari, Firefox, Edge (last 2 major versions) |
| Mobile support | iOS Safari 15+, Android Chrome 90+ |
| Responsive | Mobile-first, 320px–1920px |
