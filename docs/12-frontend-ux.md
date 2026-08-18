# 12 — Frontend UX

## Overview
This document defines the UX principles, interaction patterns, component behaviour, and mobile-first design approach for the entire platform — landing page, booking flow, and public pages.

The full landing page design system and section-by-section layout specification is in `27-landing-page-design-system.md`. This document covers the broader UX system.

---

## Design Philosophy

| Principle | Description |
|-----------|-------------|
| **Mobile First** | Design for 375px first, scale up to 1440px+ |
| **Speed** | Every interaction should feel instant or near-instant |
| **Simplicity** | No unnecessary steps, no noise, no confusion |
| **Trust** | Every element should reinforce credibility and professionalism |
| **Conversion** | Every page leads toward **BOOK A CLEANING** |
| **Premium** | The brand should feel high-quality, not generic |

---

## Responsive Breakpoints

| Name | Min Width | Target Devices |
|------|----------|----------------|
| `xs` | 320px | Small phones |
| `sm` | 375px | iPhone SE / standard mobile (PRIMARY) |
| `md` | 768px | Tablets, large phones |
| `lg` | 1024px | Small laptops, iPad Pro |
| `xl` | 1280px | Standard desktop |
| `2xl` | 1440px | Large desktop |
| `3xl` | 1920px | Wide/ultrawide desktop |

---

## Navigation

### Mobile Navigation
- Hamburger menu icon (top right)
- Full-screen or slide-in drawer menu when opened
- Large touch targets for menu items
- Clear "Book Now" CTA at the top of the menu in a brand color button

### Desktop Navigation
- Fixed/sticky top navbar
- Logo (left) + navigation links (center or right) + "Book Now" button (right)
- Transparent over the hero, transitions to solid background on scroll
- Smooth scroll behaviour for anchor links

### Navigation Items
```
Logo | Services | About | FAQ | Contact | [BOOK NOW] (button)
```

---

## Sticky Mobile CTA

On mobile, after the hero section scrolls out of view:
- A sticky bottom bar appears: **"BOOK A CLEANING →"**
- Full-width, brand-primary color
- Height: ~56px with safe-area-inset-bottom padding (for iOS home indicator)
- Disappears near the footer to avoid double CTA confusion
- Smooth slide-in animation on first appearance

```css
.sticky-mobile-cta {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 12px 24px calc(12px + env(safe-area-inset-bottom));
  background: var(--color-primary);
  z-index: 100;
}
```

---

## Motion & Animation System

### Principles
- **Purposeful**: Animate only when it adds meaning or guides attention
- **Short**: Transitions 150ms–400ms (never longer than 600ms)
- **Smooth**: Use `ease-out` or `cubic-bezier(0.4, 0, 0.2, 1)` easing
- **Performance-safe**: Use `transform` and `opacity` only (GPU-accelerated, no layout thrashing)
- **Accessible**: Respect `prefers-reduced-motion`

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Standard Animations

| Element | Animation | Duration |
|---------|-----------|---------|
| Hero text | Fade-in + slide-up on load | 600ms |
| Section headings | Fade-in on scroll enter | 400ms |
| Package cards | Staggered fade-in on scroll | 300ms per card |
| Add-on cards | Staggered fade-in | 250ms |
| Before/after slider | Smooth drag interaction | Native/CSS |
| FAQ accordion | Expand/collapse with height animation | 300ms |
| CTA buttons | Scale + shadow on hover | 150ms |
| Mobile menu | Slide-in from right | 250ms |
| Sticky CTA | Slide-up from bottom | 200ms |
| Page transitions | Fade crossfade | 200ms |

### Scroll-Driven Video (Hero)
See `27-landing-page-design-system.md` — Section 1 Hero specification for the full scroll-driven video behaviour, fallbacks, and performance requirements.

---

## Form UX

### General Rules
- Show inline error messages (not alert boxes)
- Error messages appear below the relevant field
- Success states shown with subtle green border + icon
- Required fields indicated (asterisk or "Required" label)
- No form should require more than 5 minutes to complete

### Booking Flow Forms
- Each step is a separate screen (not one long form)
- Progress indicator visible at all times (e.g., step 1 of 4)
- "Back" button available on every step
- All previously entered data preserved on back navigation (session storage)
- Mobile keyboards triggered with correct input types

### Input Types
| Field | HTML type | Notes |
|-------|----------|-------|
| Name | `text` | autocomplete="name" |
| Phone | `tel` | autocomplete="tel" |
| Email | `email` | autocomplete="email" |
| Postcode | `text` inputmode="numeric" | 4-digit AU format |
| Date | Custom calendar widget | Not browser default |
| Notes | `textarea` | Optional |

---

## Calendar / Date Picker UX

- Custom-built calendar widget (not browser native `<input type="date">`)
- Month navigation (previous / next)
- Visual differentiation of available, booked, and blocked dates
- Large touch-friendly date cells (minimum 40×40px on mobile)
- Today highlighted
- Past dates disabled
- Selected date highlighted in brand primary color
- After date selection, time slots appear below or on next step

---

## Package & Add-on Cards

### Package Card
```
┌────────────────────────────┐
│  3 BHK End of Lease        │
│  ~85–110 m²                │
│  From $350                 │
│                            │
│  ✓ All rooms cleaned       │
│  ✓ Kitchen & bathrooms     │
│  ✓ Windows inside          │
│  + more included           │
│                            │
│  [BOOK THIS PACKAGE]       │
└────────────────────────────┘
```

- Hover: lift (transform + box-shadow)
- Mobile: horizontal scroll carousel or single column stacked cards

### Add-on Card
```
┌────────────────────────────┐
│ [icon] Garden Cleaning     │
│ Professional garden tidy   │
│ + $20.00                   │
│                     [ADD]  │
└────────────────────────────┘
```

- When selected: card gets a brand-color border and checkmark
- Price shown in accent color

---

## Before / After Slider

- A horizontal drag slider reveals the "After" image over the "Before" image
- Works via mouse drag on desktop, touch drag on mobile
- Default position: 50% (equal before/after)
- Drag handle: visible, branded icon
- Labels: "Before" (left) and "After" (right), or client-preferred labels
- The slider label text is configurable (client may want different language)
- Fallback (if JS disabled or performance issue): side-by-side static images

---

## Testimonial Section

- Horizontal scroll carousel on mobile
- Grid layout on desktop
- Each card: avatar placeholder, name, review text, star rating
- Auto-scroll optional (disabled if `prefers-reduced-motion`)
- Navigation dots and/or prev/next buttons

---

## FAQ Accordion

- Click/tap to expand each FAQ item
- Smooth height animation on expand/collapse
- One item open at a time (or multiple — designer choice)
- Plus/minus icon toggles on expand/collapse
- Keyboard accessible (Enter and Space to toggle)

---

## Loading States

- Show skeleton loaders for package cards and calendar while data loads
- Spinner on payment submit button
- Disable form submit button while submitting (prevent double-submission)

---

## Toast Notifications

- Show small toast messages for:
  - Add-on selected/deselected
  - Date selected
  - Error messages
  - Success messages

---

## Related Documents
- `27-landing-page-design-system.md` — Full landing page design system
- `11-pwa-requirements.md` — PWA and mobile requirements
- `13-seo-requirements.md` — SEO considerations
- `03-user-booking-flow.md` — Booking flow UX
