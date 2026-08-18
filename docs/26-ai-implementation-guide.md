# 26 — AI Implementation Guide

## Overview
This document is a guide for the AI coding model that will implement this project. Read this document carefully before starting implementation. It explains priorities, constraints, implementation order, and key decisions.

---

## ⚠️ CRITICAL INSTRUCTIONS FOR THE IMPLEMENTING AI

### DO NOT Implement Google Calendar
**Google Calendar integration is PHASE 2 ONLY.**
- Do NOT write any Google Calendar API code.
- Do NOT require Google API credentials.
- Do NOT make any booking functionality depend on Google Calendar.
- DO include the `google_calendar_event_id` field in the Booking model (blank, unused).
- DO create a `google_calendar.py` file in the services directory with a docstring that says "Phase 2 implementation" and empty function stubs only.
- The application must work 100% without Google Calendar.

---

### ⚠️ CSS Design Tokens — Single Source of Truth

**Every color, font, spacing value, shadow, and border-radius MUST be a CSS custom property defined in `design-tokens.css`.**

> **If you change a color in one place (`design-tokens.css`), it must automatically update everywhere across the entire website.**

Rules:
- **NEVER** write a raw hex code, RGB value, or pixel size directly in a component or section CSS file.
- **ALWAYS** reference a token: `var(--color-primary)`, `var(--space-8)`, `var(--radius-lg)`.
- All design tokens are defined in `static/css/design-tokens.css` — see `28-css-architecture.md`.
- The entire design system is structured as: `design-tokens.css` → `base.css` → `layout.css` → components → sections → pages.
- Only `main.css` is linked in the HTML — it `@import`s all other CSS files.

**Correct:**
```css
.card {
  background: var(--color-bg-card);     /* ✅ token reference */
  border-radius: var(--radius-lg);       /* ✅ token reference */
  padding: var(--space-card);           /* ✅ token reference */
  box-shadow: var(--shadow-md);          /* ✅ token reference */
}
```

**Wrong:**
```css
.card {
  background: #ffffff;     /* ❌ raw value — never do this */
  border-radius: 20px;     /* ❌ magic number */
  padding: 32px;           /* ❌ magic number */
}
```

**To change the brand color:**
1. Open `static/css/design-tokens.css`
2. Update `--brand-primary-h`, `--brand-primary-s`, `--brand-primary-l`
3. Done — all buttons, cards, nav, CTAs, shadows, calendar, and section colors update automatically.

**To change the font:**
1. Open `static/css/design-tokens.css`
2. Update `--font-heading` and `--font-body`
3. Done — all typography updates everywhere.

Full CSS architecture specification: **`28-css-architecture.md`**

---

### Source of Truth
- The `/docs` directory is the complete specification.
- All architectural decisions are documented in these files.
- Do not make significant decisions that contradict the spec without flagging them.

### Do Not Hardcode Content
- Prices, package names, and add-on names must NEVER be hardcoded.
- All content must come from the database (managed via Django admin).
- Use placeholder data in Django fixtures/seed data, clearly marked.

---

## Implementation Order (Recommended)

Follow this order to build the project:

### Step 1: Project Setup
1. Create Django project with `config/settings/` structure (base, development, production)
2. Set up SQLite for development, document PostgreSQL for production
3. Install requirements: `django`, `stripe`, `htmx`, `pillow`, `whitenoise`
4. Configure environment variables (see `15-django-project-structure.md`)
5. Set up `.gitignore`, `.env.example`

### Step 1.5: CSS Architecture Setup (Do This BEFORE Writing Any Styles)
1. Create `static/css/design-tokens.css` — all color/font/spacing/shadow tokens (see `28-css-architecture.md`)
2. Create `static/css/base.css` — reset, body, headings, links (references tokens only)
3. Create `static/css/layout.css` — container, grid, section wrappers
4. Create `static/css/utilities.css` — sr-only, text helpers, flex helpers, badge
5. Create `static/css/animations.css` — all `@keyframes` and animation classes
6. Create `static/css/main.css` — `@import`s all CSS files in order
7. Create component CSS files: `components/buttons.css`, `components/cards.css`, `components/nav.css`, etc.
8. **Verify:** Run a global search — if any `.css` file other than `design-tokens.css` contains a raw hex code (`#XXXXXX`), fix it.

> The complete file structure is in `28-css-architecture.md`. Read it before creating any CSS file.

### Step 2: Database Models
1. Create all models from `17-database-schema.md`:
   - `CleaningPackage`
   - `AddOnService`
   - `TimeSlot`
   - `BlockedDate`
   - `Booking`
   - `BookingAddOn`
2. Run migrations
3. Create admin registrations for all models

### Step 3: Django Admin
1. Register all models in `admin.py`
2. Customise admin list display, filters, search for Booking
3. Create simple admin calendar view
4. Block/unblock date admin actions

### Step 4: Availability Logic
1. Implement `availability.py` service
2. Implement `get_date_status()`, `is_date_available()`, `get_available_dates()`
3. Write unit tests for all availability scenarios

### Step 5: Booking Flow (Backend)
1. Implement session-based booking state
2. Implement views for each step (1–5)
3. Implement Stripe PaymentIntent creation view
4. Implement Stripe webhook handler
5. Implement booking confirmation email

### Step 6: API Endpoints
1. `/api/availability/` — date status for calendar
2. `/api/timeslots/` — slots for selected date
3. `/api/price/` — server-side price calculation

### Step 7: Templates — Booking Flow
1. Base booking template with progress indicator
2. Step 1: Package selection
3. Step 2: Add-on selection (with live total)
4. Step 3: Date/time selection (custom calendar)
5. Step 4: Customer details form
6. Step 5: Review summary
7. Payment page (Stripe Elements)
8. Confirmation page

### Step 8: Landing Page
1. Create all 12 sections from `27-landing-page-design-system.md`
2. Hero section with video + scroll interaction
3. Trust section
4. How It Works
5. Packages (dynamic from DB)
6. Add-ons (dynamic from DB)
7. Before/After slider
8. Why Choose Us
9. Testimonials
10. Service Areas
11. FAQ
12. Final CTA
13. Footer
14. Sticky mobile CTA

### Step 9: Public Pages
1. Services/Packages page
2. About Us page
3. Contact Us page
4. FAQ page
5. Privacy Policy, Terms, Cancellation Policy

### Step 10: SEO
1. Add all meta tags to base template
2. Add JSON-LD schemas (LocalBusiness, Service, FAQ)
3. Set up sitemap with `django.contrib.sitemaps`
4. Configure `robots.txt` view
5. Ensure canonical URLs on all pages

### Step 11: PWA
1. Create Web App Manifest
2. Create Service Worker
3. Register Service Worker in base template
4. Create offline fallback page
5. Create all required PWA icons

### Step 12: Performance
1. Compress and serve static files via WhiteNoise
2. Ensure all images use WebP with fallback
3. Implement lazy loading on below-fold images
4. Preload hero poster image
5. Defer all non-critical JavaScript

### Step 13: Testing
1. Write unit tests for pricing logic
2. Write unit tests for availability logic
3. Write integration tests for booking flow
4. Write integration tests for Stripe webhook
5. Run Lighthouse audits and fix issues

### Step 14: Deployment
1. Configure production settings
2. Set up hosting (Railway/Render/VPS)
3. Configure PostgreSQL in production
4. Set up environment variables in production
5. Configure Stripe live keys and webhook URL
6. Configure SMTP email
7. Final testing in production

---

## Key Implementation Decisions

### Session-Based Booking (not model-based until payment)
- Use Django sessions to store booking state across steps
- Only create a Booking record when the customer reaches the review step
- This avoids orphaned bookings from users who abandon mid-flow

### One Booking Per Day Rule
- Use a database-level uniqueness approach (unique index on `booking_date` for confirmed bookings)
- See `08-availability-and-calendar.md` for concurrency handling

### Price Calculation
- ALWAYS calculate prices server-side
- Never trust amounts from the client
- See `09-payments.md` for the calculation logic

### Stripe Webhook as Source of Truth
- Only mark a booking as Confirmed when the Stripe webhook succeeds
- Do not rely on Stripe's redirect or client-side success callback
- See `09-payments.md` for webhook handling

---

## Google Calendar — Phase 2 Architecture Guide

> **REMINDER: Do NOT implement in MVP.**

For Phase 2 implementation, the following is pre-planned:

1. The `Booking.google_calendar_event_id` field is already in the schema.
2. Create `apps/bookings/services/google_calendar.py` with empty stubs only.
3. In Phase 2, call `create_calendar_event(booking)` asynchronously after a booking is confirmed.
4. Never block the confirmation flow on Google Calendar success — it must be a background/async operation.
5. Full Phase 2 spec in `10-google-calendar.md`.

---

## CSS / Frontend Conventions

- Use Vanilla CSS with CSS custom properties (variables) for the design system
- No TailwindCSS
- No Bootstrap
- No jQuery
- HTMX for partial updates
- Vanilla JS for scroll video, before/after slider, calendar widget
- All animations must respect `prefers-reduced-motion`
- Mobile-first CSS (default styles for mobile, `min-width` media queries for larger screens)

---

## Template Conventions

- `base.html` — full site base (head, nav, footer, PWA meta)
- `base_booking.html` — extends `base.html`, adds booking progress bar
- Use `{% block content %}` pattern
- Use HTMX attributes (`hx-get`, `hx-post`, `hx-target`, `hx-swap`) for dynamic updates
- Include CSRF token in all HTMX POST requests via `hx-headers` or Django HTMX middleware

---

## Placeholder Content Policy

- Use `[PLACEHOLDER — Replace before launch]` comments in templates
- Do NOT use real business names, phone numbers, or addresses as placeholders
- Do NOT use real people's names in placeholder reviews
- Video: use a clearly labelled placeholder MP4

---

## Fixtures / Seed Data

Create a `fixtures/initial_data.json` or management command that seeds:
- 4 placeholder packages (names only, no prices)
- 3 placeholder add-ons (names only, no prices)
- 3 default time slots: 8:00 AM, 10:00 AM, 1:00 PM

Clearly comment these as placeholders.

---

## Files That Must Exist (Even If Empty / Phase 2 Only)

| File | Status | Reason |
|------|--------|--------|
| `apps/bookings/services/google_calendar.py` | Empty stubs | Phase 2 placeholder |
| `static/video/hero-transformation.mp4` | Placeholder video | Must exist for template |
| `static/manifest.json` | Full implementation | PWA requirement |
| `static/sw.js` | Full implementation | PWA requirement |
| `templates/offline.html` | Full implementation | PWA offline fallback |

---

## Environment Variables to Document

All environment variables must be documented in `.env.example`. See `15-django-project-structure.md` for the complete list.

Google Calendar env vars:
```bash
# PHASE 2 — Leave empty in MVP
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_CALENDAR_ID=
GOOGLE_REFRESH_TOKEN=
```

---

## Related Documents (Read All Before Starting)
- `01-project-overview.md` — Project goals and tech stack
- `02-functional-requirements.md` — Full requirements
- `03-user-booking-flow.md` — Booking steps
- `05-packages.md` — Package model
- `06-addons.md` — Add-on model
- `07-booking-management.md` — Booking model
- `08-availability-and-calendar.md` — Availability logic
- `09-payments.md` — Stripe integration
- `10-google-calendar.md` — **Phase 2 only — do not implement**
- `11-pwa-requirements.md` — PWA manifest + service worker
- `13-seo-requirements.md` — SEO schemas + meta tags
- `15-django-project-structure.md` — Project layout
- `16-api-and-backend-architecture.md` — API endpoints
- `17-database-schema.md` — Full database schema
- `21-performance-strategy.md` — Video + image optimisation
- `27-landing-page-design-system.md` — Landing page specification
