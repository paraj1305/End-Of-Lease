# 22 — Development Phases

## Overview
The project is divided into two phases. Phase 1 is the MVP that must be built and launched. Phase 2 contains post-launch enhancements.

---

## PHASE 1 — MVP (Build & Launch)

### Estimated Timeline: 20–30 Working Days

| Module | Estimated Time | Priority | Notes |
|--------|---------------|---------|-------|
| Django project setup + environment | 1 day | P0 | Settings, requirements, DB, env vars |
| Database models + migrations | 1–2 days | P0 | All models from schema doc |
| Admin panel (packages, add-ons, bookings, calendar) | 3–5 days | P0 | Core management functions |
| Booking flow (all 5 steps + session management) | 4–6 days | P0 | Core customer flow |
| Availability logic + calendar | 2–3 days | P0 | One booking per day, block/unblock |
| Pricing + deposit calculation | 1 day | P0 | 10% deposit logic |
| Stripe payment integration + webhooks | 2–3 days | P0 | 10% deposit, confirmed booking |
| Email notifications | 1–2 days | P1 | Booking confirmation |
| Landing page — full design system | 4–6 days | P0 | All 12 sections, scroll video, before/after |
| Booking flow UI | 2–3 days | P0 | Mobile-first booking screens |
| Public pages (About, Contact, FAQ, Services) | 2–3 days | P1 | SEO optimised |
| PWA setup (manifest + service worker) | 1–2 days | P1 | Installable, offline fallback |
| SEO (schema, sitemap, robots, meta tags) | 1–2 days | P1 | All pages |
| Performance optimisation | 1–2 days | P1 | Video, images, Core Web Vitals |
| Testing (unit, integration, manual, browser) | 3–5 days | P0 | See testing requirements doc |
| Deployment setup | 1–2 days | P0 | Production hosting + Stripe live keys |
| Client content integration + polish | 2–3 days | P1 | After client provides content |

**Total: ~25–35 days depending on scope confirmation and content delivery**

### Phase 1 Exclusions (Do NOT Build)
- ❌ Google Calendar integration
- ❌ Customer login / accounts
- ❌ SMS / WhatsApp notifications
- ❌ Admin-editable FAQ / testimonials / service areas
- ❌ Suburb landing pages
- ❌ Review/reputation management
- ❌ Coupon / loyalty system
- ❌ Native mobile app

---

## PHASE 2 — Post-Launch Enhancements

> Phase 2 begins after Phase 1 MVP is live and the business is operational.

### Planned Phase 2 Features

#### Google Calendar Integration ⚠️ PRIORITY PHASE 2 FEATURE
- One-way sync: confirmed bookings → Google Calendar
- Admin connects their Google account via OAuth
- Cancelled bookings removed from calendar
- Existing `google_calendar_event_id` field in Booking model ready for use
- Full specification in `10-google-calendar.md`
- Estimated: 2–3 days

#### SMS / WhatsApp Notifications
- Booking confirmation SMS (Twilio or similar)
- Booking reminder 24 hours before
- Estimated: 2–3 days

#### Booking Reminder Emails
- Automated "Your cleaning is tomorrow" email
- Post-cleaning "Please leave a review" email
- Estimated: 1–2 days

#### Customer Reviews Management
- Admin can add/edit/delete testimonials from admin panel
- Reviews displayed on landing page from database
- Estimated: 1–2 days

#### FAQ Admin Management
- Admin can edit FAQ items from admin panel
- Estimated: 1 day

#### Service Area Pages
- Individual suburb landing pages for SEO
- e.g., `/cleaning/parramatta/`, `/cleaning/penrith/`
- Estimated: 3–5 days

#### Admin Content Management (Simple CMS)
- Admin can edit key homepage content (hero text, value props)
- Admin can manage service areas list
- Estimated: 2–3 days

#### Coupon / Discount System
- Admin creates discount codes
- Customer enters code during booking
- Percentage or fixed discount
- Estimated: 2–3 days

#### Advanced Admin Reporting
- Revenue reports, bookings by month, popular packages
- Export to CSV
- Estimated: 2–3 days

#### Multi-Day / Multi-Time Slot Support
- Currently: one booking per day
- Phase 2: configurable per-day capacity
- Estimated: 2–3 days

#### Customer Account (Optional)
- Allow customers to create accounts and view booking history
- Estimated: 5–8 days

---

## Phase 2 Timeline Estimate

| Feature | Estimated Time |
|---------|---------------|
| Google Calendar | 2–3 days |
| SMS/WhatsApp | 2–3 days |
| Review management | 1–2 days |
| FAQ management | 1 day |
| Suburb SEO pages | 3–5 days |
| Simple CMS | 2–3 days |
| Coupons | 2–3 days |
| Reporting | 2–3 days |

**Phase 2 total estimate: 15–23 additional days** (prioritise with client after MVP launch)

---

## Related Documents
- `23-acceptance-criteria.md`
- `24-future-enhancements.md`
- `10-google-calendar.md` (Phase 2)
