# 01 — Project Overview

## Project Name
**End of Lease Cleaning** — Professional Home Cleaning Booking Platform

---

## Project Goal
Build a premium, mobile-first home/end-of-lease cleaning service website with:
- A visually stunning landing page that immediately communicates trust and quality
- An extremely simple booking flow (no customer account required)
- Admin-managed packages, add-ons, availability, and pricing
- 10% online deposit payment via Stripe
- Booking confirmation via email
- Progressive Web App (PWA) support for mobile installability
- SEO-optimised public pages

The website should feel **premium, modern, fast, and trustworthy** — designed to convert visitors into customers at a high rate.

---

## Design Inspiration
| Reference | Role |
|-----------|------|
| [moveoutcleaning.au](https://moveoutcleaning.au/) | **Primary UX/design inspiration** — overall landing page experience, section flow, visual hierarchy, spacing, interactions and premium cleaning-service feel |
| [sparkleclean.au](https://sparkleclean.au/) | Secondary inspiration for landing page |
| Competitor sites (exitcleaners, kleeningcrew, freshallseasons, etc.) | Market research only |

> **Important:** The final design must be ORIGINAL. Do not copy logos, brand names, copyrighted images/video, exact text, proprietary assets, or source code from any reference site. Use these references only for UX/design direction and experience quality benchmarking.

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django (Python) |
| Frontend | Django Templates + HTMX + Vanilla JS |
| CSS | Vanilla CSS (no Tailwind unless requested) |
| Database | SQLite (development) → PostgreSQL (production) |
| PWA | Web App Manifest + Service Worker |
| Payments | Stripe (10% deposit) |
| Google Calendar | **PHASE 2 ONLY — NOT in MVP** |
| Hosting | Cloud hosting with HTTPS (e.g., Railway, Render, or VPS) |
| Email | Django email / SMTP (booking confirmations) |

---

## Target Users

### Customers (Public)
- Residential tenants moving out of a property
- Homeowners needing end-of-lease or general cleaning
- Users who prefer booking online without creating an account

### Admin / Business Owner
- Single admin or small team managing the business
- Needs to manage packages, prices, availability, and bookings from a web dashboard

---

## MVP Scope

### Included in MVP
- [x] Mobile-first, premium landing page
- [x] PWA support (installable on mobile)
- [x] 4–5 SEO-optimised public pages
- [x] Cleaning package selection (from admin-managed catalogue)
- [x] Add-on service selection
- [x] Automatic booking price calculation
- [x] Date/time slot selection (one appointment per day)
- [x] No customer login required
- [x] Basic customer information form
- [x] 10% online advance payment via Stripe
- [x] Booking confirmation page + email
- [x] Admin dashboard (bookings, packages, add-ons, calendar, payments)
- [x] Admin calendar with blocked/booked/available dates
- [x] Date blocking/unblocking from admin
- [x] Scroll-driven video hero section (dirty→clean transformation)
- [x] Before/after image slider section

### Explicitly Out of MVP Scope
- [ ] Google Calendar sync → **PHASE 2**
- [ ] Customer account/login system
- [ ] Native Android/iOS application
- [ ] Multi-cleaner marketplace
- [ ] Employee payroll system
- [ ] Advanced CRM
- [ ] Real-time chat
- [ ] Recurring subscription bookings
- [ ] Complex coupon/loyalty system
- [ ] SMS/WhatsApp confirmation (can be Phase 2)

---

## Public Pages (MVP)
1. **Home / Landing Page** — Primary conversion page with all key sections
2. **Cleaning Services / Packages** — Detailed service listing
3. **About Us** — Business story and trust signals
4. **Contact Us** — Contact form and business info
5. **FAQ** — Common questions and answers
6. *(Optional)* **Booking** — Dedicated booking page or modal

---

## Key Business Rules
1. Only **one appointment can be booked per day**.
2. Once a date is booked, it becomes automatically unavailable.
3. Admin can manually block/unblock any date.
4. Customer pays **10% of total (package + add-ons)** as a deposit.
5. Booking is confirmed only after successful Stripe payment.
6. No customer account is needed at any stage.
7. All package/add-on prices are managed exclusively from the admin panel.

---

## Items Still to Confirm with Client
See `25-open-questions.md` for the full list.

Key items pending:
- Final package names, square-foot ranges, and prices
- Final add-on list and prices
- Target country/currency (assumed: Australia / AUD)
- Preferred payment gateway (assumed: Stripe)
- Available booking hours/time slots
- Whether 10% deposit is calculated before or after add-ons/taxes
- Cancellation/refund policy
- Customer confirmation method (email assumed; SMS/WhatsApp Phase 2)
- Brand logo, colors, final images
- Final suburb/city service area list
- Final terms and conditions content
- Final FAQ content
