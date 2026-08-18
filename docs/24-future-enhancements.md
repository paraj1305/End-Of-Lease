# 24 — Future Enhancements

## Overview
This document lists all features that are explicitly out of scope for the MVP but have been identified as potential future enhancements. These should be designed around in the MVP architecture where possible.

---

## PHASE 2 — High Priority

### 1. Google Calendar Integration ⭐ PRIORITY
- **Status:** Phase 2 — NOT in MVP
- **Description:** One-way sync of confirmed bookings to the business's Google Calendar
- **Architecture readiness:** `google_calendar_event_id` field already in Booking model
- **Full spec:** See `10-google-calendar.md`
- **Estimated effort:** 2–3 days

### 2. SMS / WhatsApp Notifications
- **Status:** Phase 2
- **Description:** Send booking confirmation and reminders via SMS (Twilio) or WhatsApp Business API
- **Architecture readiness:** Email service is abstracted — adding SMS is additive
- **Estimated effort:** 2–3 days

### 3. Booking Reminders
- **Status:** Phase 2
- **Description:** Automated emails 24h and 2h before the cleaning appointment
- **Estimated effort:** 1–2 days (requires Celery beat or cron)

### 4. Admin-Managed Testimonials
- **Status:** Phase 2
- **Description:** Admin adds/edits real customer reviews; displayed on landing page from database
- **Architecture readiness:** Testimonials section already on landing page with placeholder data
- **Estimated effort:** 1–2 days

### 5. Admin-Managed FAQ
- **Status:** Phase 2
- **Description:** FAQ items editable from admin panel
- **Architecture readiness:** FAQ section on landing page uses template; convert to model
- **Estimated effort:** 1 day

### 6. Service Area Suburb Landing Pages
- **Status:** Phase 2
- **Description:** Individual SEO pages per suburb (e.g., `/cleaning/parramatta/`)
- **Architecture readiness:** Service area section on landing page uses placeholder text
- **Estimated effort:** 3–5 days

---

## PHASE 2 — Medium Priority

### 7. Coupon / Discount System
- **Status:** Phase 2
- **Description:** Admin creates discount codes (% or fixed); customer enters during booking
- **Estimated effort:** 2–3 days

### 8. Admin Reporting
- **Status:** Phase 2
- **Description:** Revenue reports, bookings by month, popular packages, export to CSV
- **Estimated effort:** 2–3 days

### 9. Admin Content Management (Simple CMS)
- **Status:** Phase 2
- **Description:** Admin can edit hero text, value props, service areas from admin panel
- **Estimated effort:** 2–3 days

### 10. Post-Cleaning Review Requests
- **Status:** Phase 2
- **Description:** Automated email after job is marked Complete, requesting a review (Google / direct)
- **Estimated effort:** 1–2 days

### 11. Multi-Day Capacity
- **Status:** Phase 2
- **Description:** Allow more than one booking per day (configurable daily capacity)
- **Current rule:** One booking per day (MVP)
- **Estimated effort:** 2–3 days (availability logic refactor)

---

## PHASE 3 — Lower Priority / Larger Scope

### 12. Customer Accounts
- **Status:** Phase 3
- **Description:** Optional customer login to view booking history, re-book, manage details
- **Estimated effort:** 5–8 days

### 13. Native Mobile App
- **Status:** Phase 3 / Out of Scope
- **Description:** React Native or Flutter app
- **Note:** PWA in Phase 1 reduces urgency significantly

### 14. Multi-Cleaner / Staff Management
- **Status:** Phase 3 / Out of Scope
- **Description:** Assign jobs to individual cleaners, view cleaner availability
- **Estimated effort:** 10–15+ days

### 15. Subscription / Recurring Bookings
- **Status:** Phase 3
- **Description:** Regular cleaning schedule (weekly, fortnightly, monthly)
- **Estimated effort:** 5–8 days

### 16. Real-Time Chat / Support
- **Status:** Phase 3 / Out of Scope
- **Description:** Live chat widget for customer support
- **Estimated effort:** 2–3 days (third-party integration e.g. Crisp, Intercom)

### 17. Advanced CRM
- **Status:** Phase 3 / Out of Scope
- **Description:** Full customer management, communication history, follow-ups
- **Estimated effort:** 15+ days

### 18. Loyalty / Points System
- **Status:** Phase 3 / Out of Scope
- **Description:** Reward repeat customers with points or discounts

---

## Architecture Readiness Summary

| Future Feature | Architecture Ready in MVP? |
|---------------|--------------------------|
| Google Calendar | ✅ `google_calendar_event_id` field in Booking model |
| SMS notifications | ✅ Email service abstracted |
| Testimonials from DB | ✅ Section in template; easy to convert |
| FAQ from DB | ✅ Section in template; easy to convert |
| Suburb SEO pages | ✅ URL structure designed for it |
| Discount codes | ⚠️ Minor pricing logic addition needed |
| Multi-day capacity | ⚠️ Availability logic refactor needed |
| Customer accounts | ❌ Significant architectural addition |
| Multi-cleaner | ❌ Major feature requiring new models |

---

## Related Documents
- `10-google-calendar.md` (Phase 2 spec)
- `22-development-phases.md`
- `25-open-questions.md`
