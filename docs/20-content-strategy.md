# 20 — Content Strategy

## Overview
This document defines the content strategy for the MVP — what content is needed, where it comes from (client vs. placeholder), and what is static vs. admin-managed.

---

## Content Sources

| Content Item | Source | Status |
|-------------|--------|--------|
| Business name | Client | ⏳ Pending |
| Logo | Client | ⏳ Pending |
| Brand colors | Client | ⏳ Pending |
| Hero video (transformation) | Client / Licensed | ⏳ Pending |
| Package names | Client | ⏳ Pending |
| Package prices | Client | ⏳ Pending |
| Package descriptions | Client | ⏳ Pending |
| Add-on names + prices | Client | ⏳ Pending |
| Service area list (suburbs) | Client | ⏳ Pending |
| Terms & Conditions | Client / Legal | ⏳ Pending |
| Cancellation Policy | Client | ⏳ Pending |
| FAQ content | Client | ⏳ Pending |
| Customer reviews | Client (real) | ⏳ Pending |
| Business address | Client | ⏳ Pending |
| Business phone | Client | ⏳ Pending |
| Social media links | Client | ⏳ Pending |
| About Us story | Client | ⏳ Pending |
| Before/after photos | Client / Licensed | ⏳ Pending |

---

## Placeholder Content Rules

1. **Hero video**: Use a clearly labelled placeholder MP4 with the text overlay "PLACEHOLDER — Replace with licensed cleaning transformation video". Document the video spec (dimensions, codec, duration).

2. **Before/after photos**: Use placeholder images labelled "[BEFORE PHOTO — Provide licensed image]" and "[AFTER PHOTO — Provide licensed image]".

3. **Reviews**: Display clearly marked "PLACEHOLDER REVIEW — Replace with real customer testimonial" cards. Do NOT use fabricated customer names or fake reviews that could be mistaken for real ones.

4. **Service areas**: Use "[SUBURB LIST — To be provided by client]" placeholder text in the service area section.

5. **Prices**: All prices must be entered by the client in the admin panel before launch. No prices are hardcoded.

---

## Admin-Managed Content (MVP)

The following content is managed exclusively through the Django admin panel:
- Cleaning packages (name, area, price, description, included services, status)
- Add-on services (name, description, price, status)
- Booking availability (time slots, blocked dates)
- Business settings (name, contact, deposit %)

---

## Static Content (MVP — Update Before Launch)

The following content is in templates and must be reviewed/updated before launch:
- Hero headline and subheading
- "Why Choose Us" section
- "How It Works" steps
- FAQ questions and answers
- Terms & Conditions
- Privacy Policy
- Cancellation Policy
- About Us page content
- Footer links

---

## Phase 2 Admin-Managed Content

In Phase 2, consider making these admin-editable:
- FAQ items
- Testimonials / reviews
- Service areas list
- Homepage hero headline
- "Why Choose Us" content
- Trust signals / value props

---

## Hero Video Specification

The final hero video should meet these technical requirements:
| Spec | Requirement |
|------|------------|
| Duration | 30–60 seconds (for scroll interaction) or 10–15 sec loop |
| Concept | Dirty/messy room → clean/organized (transformation) |
| Aspect ratio | 16:9 (desktop); optionally 9:16 for mobile crop |
| Format | MP4 (H.264) + WebM (VP9) |
| Resolution | 1920×1080 max (1280×720 acceptable) |
| File size | < 10 MB (compressed for web) |
| Codecs | H.264 + AAC (MP4), VP9 (WebM) |
| Audio | No audio needed (muted autoplay) |
| Poster image | WebP, 1920×1080, < 200 KB |
| Mobile version | Optional: lower resolution/bitrate mobile version |

> Do NOT use copyrighted video from reference websites. Source or create original licensed content.

---

## Related Documents
- `01-project-overview.md`
- `25-open-questions.md`
- `27-landing-page-design-system.md`
