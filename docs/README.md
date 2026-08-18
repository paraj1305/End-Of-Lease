# End of Lease Cleaning — Documentation Index

> **This `/docs` directory is the single source of truth for the entire project.**
> All design decisions, architecture choices, business rules, and implementation requirements live here.
> The next AI coding model must read all relevant documents before starting implementation.

---

## Project Summary

A premium, mobile-first **end of lease cleaning service website** with:
- Visually stunning landing page with scroll-driven video hero
- 5-step booking flow (no customer account required)
- 10% deposit payment via Stripe
- Admin panel for packages, add-ons, availability, bookings
- PWA (installable on mobile)
- SEO-optimised public pages
- Google Calendar: **PHASE 2 ONLY — NOT in MVP**

---

## Quick Reference

| Topic | Document |
|-------|---------|
| 🚀 Start here | [`01-project-overview.md`](./01-project-overview.md) |
| 🤖 AI coding guide | [`26-ai-implementation-guide.md`](./26-ai-implementation-guide.md) |
| 🎨 Landing page spec | [`27-landing-page-design-system.md`](./27-landing-page-design-system.md) |
| 🎨 CSS design tokens | [`28-css-architecture.md`](./28-css-architecture.md) |
| 📦 MVP scope & phases | [`22-development-phases.md`](./22-development-phases.md) |
| ✅ Acceptance criteria | [`23-acceptance-criteria.md`](./23-acceptance-criteria.md) |
| ❓ Open questions | [`25-open-questions.md`](./25-open-questions.md) |

---

## Document List

### Core Requirements
| File | Description |
|------|-------------|
| [`01-project-overview.md`](./01-project-overview.md) | Project goals, tech stack, MVP scope, design inspiration |
| [`02-functional-requirements.md`](./02-functional-requirements.md) | Full functional requirements (all features) |
| [`03-user-booking-flow.md`](./03-user-booking-flow.md) | Step-by-step customer booking journey |
| [`04-admin-panel.md`](./04-admin-panel.md) | Admin dashboard, management interfaces |

### Feature Specifications
| File | Description |
|------|-------------|
| [`05-packages.md`](./05-packages.md) | Cleaning package model and admin management |
| [`06-addons.md`](./06-addons.md) | Add-on services model and admin management |
| [`07-booking-management.md`](./07-booking-management.md) | Booking model, status lifecycle, business rules |
| [`08-availability-and-calendar.md`](./08-availability-and-calendar.md) | Date availability, one-booking-per-day rule |
| [`09-payments.md`](./09-payments.md) | Stripe payment integration and deposit logic |
| [`10-google-calendar.md`](./10-google-calendar.md) | **⚠️ PHASE 2 ONLY** — Google Calendar integration spec |

### Frontend & UX
| File | Description |
|------|-------------|
| [`11-pwa-requirements.md`](./11-pwa-requirements.md) | PWA manifest, service worker, offline support |
| [`12-frontend-ux.md`](./12-frontend-ux.md) | UX principles, navigation, motion system, components |
| [`13-seo-requirements.md`](./13-seo-requirements.md) | SEO schemas, sitemap, meta tags, URL structure |
| [`27-landing-page-design-system.md`](./27-landing-page-design-system.md) | 🌟 Complete landing page design system + all 12 sections |

### Backend & Infrastructure
| File | Description |
|------|-------------|
| [`14-email-notifications.md`](./14-email-notifications.md) | Email confirmation templates and configuration |
| [`15-django-project-structure.md`](./15-django-project-structure.md) | Project layout, file structure, environment vars |
| [`16-api-and-backend-architecture.md`](./16-api-and-backend-architecture.md) | URL routes, API endpoints, session management |
| [`17-database-schema.md`](./17-database-schema.md) | Full database schema with all tables and indexes |
| [`18-deployment.md`](./18-deployment.md) | Production hosting and deployment requirements |

### Quality & Strategy
| File | Description |
|------|-------------|
| [`19-testing-requirements.md`](./19-testing-requirements.md) | Unit tests, integration tests, browser testing |
| [`20-content-strategy.md`](./20-content-strategy.md) | Content sources, placeholders, hero video spec |
| [`21-performance-strategy.md`](./21-performance-strategy.md) | Video optimisation, Core Web Vitals, caching |

### Project Management
| File | Description |
|------|-------------|
| [`22-development-phases.md`](./22-development-phases.md) | Phase 1 (MVP) and Phase 2 roadmap with timeline |
| [`23-acceptance-criteria.md`](./23-acceptance-criteria.md) | Handover checklist and MVP acceptance criteria |
| [`24-future-enhancements.md`](./24-future-enhancements.md) | Post-launch feature roadmap |
| [`25-open-questions.md`](./25-open-questions.md) | Pending client confirmations |
| [`26-ai-implementation-guide.md`](./26-ai-implementation-guide.md) | Guide for the AI model implementing this project |

---

## ⚠️ Critical Rules (Summary)

1. **Google Calendar = PHASE 2. Do NOT implement in MVP.**
2. **Never hardcode prices.** All prices come from the admin database.
3. **Mobile first.** Design and test on 375px screen first.
4. **Stripe webhook = source of truth for payment.** Never rely on client-side payment confirmation.
5. **One booking per day.** Database-enforced.
6. **No customer login required.** The entire flow works without an account.
7. **All important content in crawlable HTML.** Video does not replace text content.
8. **Placeholder content must be clearly labelled.** Never use fabricated real reviews or contact info.

---

## Consistency Check

| Flow | Connected To |
|------|-------------|
| Landing page → Booking | Every CTA links to `/book/` |
| Booking → Package system | Packages loaded from CleaningPackage model |
| Booking → Add-on system | Add-ons from AddOnService model |
| Pricing → Deposit | 10% of (package + add-ons), calculated server-side |
| Deposit → Stripe | Stripe PaymentIntent in AUD |
| Stripe → Booking confirmation | Webhook sets status=CONFIRMED, sends email |
| Booking → Availability | Confirmed booking blocks the date |
| Availability → Admin calendar | Admin sees all states (available/booked/blocked) |
| Admin calendar → Blocked dates | BlockedDate model, admin can block/unblock |
| PWA → Mobile UX | Manifest + service worker, installable, offline fallback |
| Video → Performance | Compressed, poster image, lazy loading, fallback |
| Landing page → SEO | All meta, schema, H1, canonical, sitemap |
| Google Calendar → Future | Field reserved, no implementation in MVP |

---

*Last updated: August 2026 | Version: 1.0 (Phase 1 MVP Specification)*
