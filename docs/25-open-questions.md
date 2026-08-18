# 25 — Open Questions

## Overview
This document tracks all items that require confirmation from the client before development can be finalised. Items should be resolved before the booking system and pricing logic are built.

---

## 🔴 CRITICAL — Must Resolve Before Development

| # | Question | Default / Assumption | Status |
|---|----------|---------------------|--------|
| OQ-01 | What are the final package names, approximate square-foot/m² ranges, and prices? | 2 BHK, 3 BHK, 4 BHK, 5 BHK — prices TBD | ⏳ Pending |
| OQ-02 | What are the final add-on services and their prices? | Garden, Garage, Bathroom deep clean — prices TBD | ⏳ Pending |
| OQ-03 | What is the target country and currency? | Australia / AUD | ✅ Assumed |
| OQ-04 | Is Stripe the preferred payment gateway? | Yes | ✅ Assumed |
| OQ-05 | Is the 10% deposit calculated on package + add-ons (subtotal) or package only? | Package + add-ons (full subtotal) | ⚠️ Assumed — confirm |
| OQ-06 | What are the available booking hours/time slots? | TBD | ⏳ Pending |
| OQ-07 | What is the cancellation/refund policy? | TBD | ⏳ Pending |
| OQ-08 | What is the confirmation method? Email only or SMS/WhatsApp too? | Email only for MVP | ✅ Assumed |

---

## 🟡 IMPORTANT — Needed Before Launch

| # | Question | Default / Assumption | Status |
|---|----------|---------------------|--------|
| OQ-09 | What is the brand name and logo? | Placeholder | ⏳ Pending |
| OQ-10 | What are the final brand colors? | Placeholder color system | ⏳ Pending |
| OQ-11 | What is the business address, phone number, and email? | Placeholder | ⏳ Pending |
| OQ-12 | What is the final list of service areas (suburbs/cities)? | Placeholder | ⏳ Pending |
| OQ-13 | What are the final FAQ questions and answers? | Placeholder content | ⏳ Pending |
| OQ-14 | Is there a minimum advance booking period? (Same day? 24h? 48h?) | 0 days (same day allowed) | ⚠️ Assumed — confirm |
| OQ-15 | What is the maximum advance booking period? | 90 days | ⚠️ Assumed — confirm |
| OQ-16 | What is the Terms & Conditions content? | Template placeholder | ⏳ Pending |
| OQ-17 | What is the Privacy Policy content? | Template placeholder | ⏳ Pending |
| OQ-18 | What is the Cancellation Policy content? | Template placeholder | ⏳ Pending |
| OQ-19 | Are there any social media profiles to link? | None for now | ⏳ Pending |

---

## 🟢 NICE TO HAVE — Pre-Launch

| # | Question | Notes |
|---|----------|-------|
| OQ-20 | Hero video: does the client have their own cleaning transformation video, or do we need to source licensed content? | Placeholder video until client provides |
| OQ-21 | Before/after photos: does the client have licensed photos of their work? | Placeholder images until client provides |
| OQ-22 | What are the final About Us page content and business story? | Template placeholder |
| OQ-23 | Does the client want Google Analytics or Tag Manager? | Not included by default — add if requested |
| OQ-24 | Does the client have any existing customer reviews to use on the website? | Placeholder until provided |
| OQ-25 | What estimated cleaning duration per package? (Used for Google Calendar events in Phase 2) | Phase 2 question |
| OQ-26 | Which Google account/calendar should Phase 2 Google Calendar sync to? | Phase 2 question |

---

## Phase 2 Open Questions

| # | Question |
|---|---------|
| OQ-P2-01 | Which Google Calendar account to connect? |
| OQ-P2-02 | Should customers receive SMS confirmation? Which SMS provider? |
| OQ-P2-03 | How many bookings per day should be allowed in Phase 2? |
| OQ-P2-04 | Should coupon/discount codes be implemented in Phase 2? |

---

## How to Update This Document

When a question is resolved:
1. Change Status from `⏳ Pending` to `✅ Confirmed`
2. Update the Default/Assumption column with the confirmed value
3. Update the relevant specification document(s)
4. Note the date confirmed

---

## Related Documents
- `01-project-overview.md`
- `05-packages.md`
- `06-addons.md`
- `09-payments.md`
- `20-content-strategy.md`
