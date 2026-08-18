# 28 — CSS Architecture & Design Tokens

## Overview

Every design value — colors, fonts, spacing, radius, shadows — must be defined **once** as a CSS custom property (CSS variable). Changing a value in one place (`design-tokens.css`) must automatically update it everywhere across the entire website.

> **This is a hard rule. No magic numbers. No hex codes scattered in component files. Every value references a token.**

---

## File Structure

```
static/
└── css/
    ├── design-tokens.css       ← SINGLE SOURCE OF TRUTH for all design values
    ├── base.css                ← Reset, root HTML/body styles, typography base
    ├── layout.css              ← Container, grid, section wrappers
    ├── components/
    │   ├── buttons.css         ← All button variants
    │   ├── cards.css           ← Package cards, add-on cards, testimonial cards
    │   ├── nav.css             ← Navigation, mobile menu
    │   ├── hero.css            ← Hero section, video, overlay, text
    │   ├── calendar.css        ← Date picker, time slot grid
    │   ├── before-after.css    ← Before/after image slider
    │   ├── accordion.css       ← FAQ accordion
    │   ├── forms.css           ← All form inputs, labels, errors
    │   ├── footer.css          ← Footer layout
    │   └── sticky-cta.css      ← Mobile sticky bottom CTA
    ├── sections/
    │   ├── trust.css           ← Trust/value props section
    │   ├── how-it-works.css    ← Numbered steps section
    │   ├── packages.css        ← Packages grid section
    │   ├── addons.css          ← Add-ons section
    │   ├── why-choose-us.css   ← Benefits section
    │   ├── testimonials.css    ← Reviews section
    │   ├── service-areas.css   ← Suburb tags section
    │   ├── faq-section.css     ← FAQ section
    │   └── final-cta.css       ← Final CTA section
    ├── pages/
    │   ├── booking.css         ← Booking flow pages
    │   ├── services.css        ← Services page
    │   ├── about.css           ← About page
    │   ├── contact.css         ← Contact page
    │   └── confirmation.css    ← Booking confirmation page
    ├── utilities.css           ← Utility/helper classes (sr-only, visually-hidden, etc.)
    ├── animations.css          ← All @keyframes and transition classes
    └── main.css                ← Imports all of the above in order (single <link> tag in HTML)
```

**Only `main.css` is linked in the HTML:**
```html
<link rel="stylesheet" href="/static/css/main.css">
```

`main.css` uses `@import` to pull in all other files:
```css
/* main.css */
@import url('./design-tokens.css');
@import url('./base.css');
@import url('./layout.css');
@import url('./utilities.css');
@import url('./animations.css');
@import url('./components/buttons.css');
@import url('./components/cards.css');
/* ... etc */
```

---

## design-tokens.css — The Single Source of Truth

```css
/**
 * =============================================================
 * DESIGN TOKENS — END OF LEASE CLEANING
 * =============================================================
 * This file is the SINGLE SOURCE OF TRUTH for all design values.
 *
 * HOW TO CHANGE THE BRAND COLOR:
 *   1. Find the relevant token in this file (e.g. --color-primary)
 *   2. Change the value here
 *   3. That's it — it updates everywhere automatically.
 *
 * DO NOT use raw hex/rgb values anywhere else in the codebase.
 * Always reference a token: var(--token-name)
 * =============================================================
 */

:root {

  /* ============================================================
   * BRAND IDENTITY — Update these when client provides brand
   * ============================================================ */

  /**
   * PRIMARY BRAND COLOR
   * Replace this to change the main brand color across the whole site.
   * Used in: navigation, buttons, headings, highlights, accents.
   */
  --brand-primary-h: 212;           /* Hue */
  --brand-primary-s: 77%;           /* Saturation */
  --brand-primary-l: 28%;           /* Lightness */
  --color-primary: hsl(var(--brand-primary-h), var(--brand-primary-s), var(--brand-primary-l));
  --color-primary-light: hsl(var(--brand-primary-h), var(--brand-primary-s), 40%);
  --color-primary-lighter: hsl(var(--brand-primary-h), var(--brand-primary-s), 55%);
  --color-primary-dark: hsl(var(--brand-primary-h), var(--brand-primary-s), 18%);
  --color-primary-alpha-10: hsla(var(--brand-primary-h), var(--brand-primary-s), var(--brand-primary-l), 0.10);
  --color-primary-alpha-20: hsla(var(--brand-primary-h), var(--brand-primary-s), var(--brand-primary-l), 0.20);

  /**
   * ACCENT COLOR
   * Used for highlights, badges, price labels, icon accents.
   */
  --brand-accent-h: 195;
  --brand-accent-s: 100%;
  --brand-accent-l: 42%;
  --color-accent: hsl(var(--brand-accent-h), var(--brand-accent-s), var(--brand-accent-l));
  --color-accent-light: hsl(var(--brand-accent-h), var(--brand-accent-s), 60%);
  --color-accent-dark: hsl(var(--brand-accent-h), var(--brand-accent-s), 28%);

  /* ============================================================
   * NEUTRAL PALETTE
   * ============================================================ */
  --color-white:        #FFFFFF;
  --color-off-white:    #F8F9FA;
  --color-grey-50:      #F9FAFB;
  --color-grey-100:     #F3F4F6;
  --color-grey-200:     #E5E7EB;
  --color-grey-300:     #D1D5DB;
  --color-grey-400:     #9CA3AF;
  --color-grey-500:     #6B7280;
  --color-grey-600:     #4B5563;
  --color-grey-700:     #374151;
  --color-grey-800:     #1F2937;
  --color-grey-900:     #111827;
  --color-near-black:   #0D1117;

  /* ============================================================
   * SEMANTIC / STATE COLORS
   * ============================================================ */
  --color-success:      #059669;   /* Available date, success messages */
  --color-success-bg:   #D1FAE5;
  --color-error:        #DC2626;   /* Booked/blocked date, error messages */
  --color-error-bg:     #FEE2E2;
  --color-warning:      #D97706;
  --color-warning-bg:   #FEF3C7;
  --color-info:         var(--color-accent);
  --color-info-bg:      #E0F7FA;

  /* ============================================================
   * SURFACE / BACKGROUND COLORS
   * ============================================================ */
  --color-bg-body:      var(--color-white);
  --color-bg-alt:       var(--color-off-white);          /* Alternating sections */
  --color-bg-dark:      #0F1923;                         /* Dark sections (Why Choose Us) */
  --color-bg-hero-overlay: rgba(10, 20, 40, 0.55);       /* Video overlay */
  --color-bg-card:      var(--color-white);
  --color-bg-nav:       rgba(15, 25, 35, 0.92);          /* Sticky nav background */
  --color-bg-footer:    #0D1117;

  /* ============================================================
   * TEXT COLORS
   * ============================================================ */
  --color-text-primary:   var(--color-grey-900);
  --color-text-secondary: var(--color-grey-500);
  --color-text-muted:     var(--color-grey-400);
  --color-text-on-dark:   var(--color-white);
  --color-text-on-primary: var(--color-white);
  --color-text-link:      var(--color-primary);
  --color-text-price:     var(--color-primary);          /* Pricing amounts */

  /* ============================================================
   * TYPOGRAPHY — FONTS
   * Change font family in one place here.
   * ============================================================ */

  /**
   * HEADING FONT
   * Replace 'Inter' with client's brand font if provided.
   */
  --font-heading: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

  /**
   * BODY FONT
   * Replace with brand body font if different from heading.
   */
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

  /**
   * MONOSPACE (for reference numbers, booking refs, etc.)
   */
  --font-mono: 'SFMono-Regular', 'Consolas', monospace;

  /* ============================================================
   * TYPOGRAPHY — SIZE SCALE (fluid / clamp-based)
   * These scale smoothly from mobile to desktop.
   * ============================================================ */
  --text-2xs:   clamp(0.625rem,  1vw,  0.75rem);   /*  10–12px */
  --text-xs:    clamp(0.75rem,   1vw,  0.8125rem);  /*  12–13px */
  --text-sm:    clamp(0.8125rem, 1.5vw, 0.875rem);  /*  13–14px */
  --text-base:  clamp(0.9375rem, 1.5vw, 1rem);      /*  15–16px */
  --text-md:    clamp(1rem,      2vw,   1.125rem);   /*  16–18px */
  --text-lg:    clamp(1.125rem,  2.5vw, 1.25rem);   /*  18–20px */
  --text-xl:    clamp(1.25rem,   3vw,   1.5rem);    /*  20–24px */
  --text-2xl:   clamp(1.5rem,    3.5vw, 2rem);      /*  24–32px */
  --text-3xl:   clamp(1.75rem,   4.5vw, 2.5rem);    /*  28–40px */
  --text-4xl:   clamp(2rem,      5.5vw, 3.5rem);    /*  32–56px */
  --text-hero:  clamp(2.25rem,   8vw,   5rem);       /*  36–80px */

  /* ============================================================
   * TYPOGRAPHY — WEIGHT
   * ============================================================ */
  --weight-regular:   400;
  --weight-medium:    500;
  --weight-semibold:  600;
  --weight-bold:      700;
  --weight-extrabold: 800;

  /* ============================================================
   * TYPOGRAPHY — LINE HEIGHT
   * ============================================================ */
  --leading-none:     1;
  --leading-tight:    1.2;
  --leading-snug:     1.375;
  --leading-normal:   1.5;
  --leading-relaxed:  1.65;
  --leading-loose:    2;

  /* ============================================================
   * TYPOGRAPHY — LETTER SPACING
   * ============================================================ */
  --tracking-tight:   -0.025em;
  --tracking-normal:  0em;
  --tracking-wide:    0.025em;
  --tracking-wider:   0.05em;
  --tracking-widest:  0.1em;

  /* ============================================================
   * SPACING SCALE — 4px base grid
   * ============================================================ */
  --space-px:   1px;
  --space-0-5:  2px;
  --space-1:    4px;
  --space-2:    8px;
  --space-3:    12px;
  --space-4:    16px;
  --space-5:    20px;
  --space-6:    24px;
  --space-7:    28px;
  --space-8:    32px;
  --space-9:    36px;
  --space-10:   40px;
  --space-12:   48px;
  --space-14:   56px;
  --space-16:   64px;
  --space-20:   80px;
  --space-24:   96px;
  --space-28:   112px;
  --space-32:   128px;

  /* Semantic spacing */
  --space-section-y:  clamp(60px, 8vw, 120px);    /* Vertical section padding */
  --space-section-x:  clamp(20px, 5vw, 80px);     /* Horizontal section padding */
  --space-card:       clamp(20px, 3vw, 40px);      /* Card padding */
  --space-gap:        clamp(16px, 2.5vw, 32px);    /* Gap between cards/items */

  /* ============================================================
   * LAYOUT
   * ============================================================ */
  --container-max:       1280px;   /* Max content width */
  --container-narrow:    760px;    /* Narrow content (blog, FAQ) */
  --container-wide:      1440px;   /* Wide content */
  --nav-height:          72px;     /* Fixed nav height */
  --sticky-cta-height:   64px;     /* Mobile sticky CTA height */

  /* ============================================================
   * BORDER RADIUS
   * ============================================================ */
  --radius-none:  0;
  --radius-xs:    4px;
  --radius-sm:    6px;
  --radius-md:    12px;
  --radius-lg:    20px;
  --radius-xl:    28px;
  --radius-2xl:   40px;
  --radius-full:  9999px;          /* Pills, avatars, tags */

  /* ============================================================
   * BORDERS
   * ============================================================ */
  --border-width:         1px;
  --border-width-thick:   2px;
  --border-color:         var(--color-grey-200);
  --border-color-dark:    var(--color-grey-700);
  --border-color-primary: var(--color-primary);

  /* ============================================================
   * SHADOWS
   * ============================================================ */
  --shadow-xs:    0 1px 2px rgba(0,0,0,0.05);
  --shadow-sm:    0 1px 3px rgba(0,0,0,0.08),  0 1px 2px rgba(0,0,0,0.05);
  --shadow-md:    0 4px 16px rgba(0,0,0,0.10), 0 2px 6px rgba(0,0,0,0.06);
  --shadow-lg:    0 12px 40px rgba(0,0,0,0.14), 0 4px 12px rgba(0,0,0,0.08);
  --shadow-xl:    0 24px 60px rgba(0,0,0,0.18);
  --shadow-2xl:   0 40px 80px rgba(0,0,0,0.22);

  /* Brand-colored shadows (for CTAs and highlighted cards) */
  --shadow-primary-sm:  0 4px 16px var(--color-primary-alpha-20);
  --shadow-primary-md:  0 8px 24px var(--color-primary-alpha-20);
  --shadow-primary-lg:  0 12px 40px rgba(15, 76, 129, 0.35);
  --shadow-cta:         0 8px 24px rgba(15, 76, 129, 0.40);

  /* Inset shadow (for pressed/active states) */
  --shadow-inset:       inset 0 2px 4px rgba(0,0,0,0.08);

  /* ============================================================
   * TRANSITIONS & ANIMATIONS
   * ============================================================ */
  --transition-fast:    150ms ease-out;
  --transition-base:    200ms ease-out;
  --transition-slow:    300ms ease-out;
  --transition-slower:  400ms ease-out;

  --ease-out:           cubic-bezier(0.4, 0, 0.2, 1);
  --ease-in:            cubic-bezier(0.4, 0, 1, 1);
  --ease-in-out:        cubic-bezier(0.4, 0, 0.2, 1);
  --ease-bounce:        cubic-bezier(0.34, 1.56, 0.64, 1);

  /* ============================================================
   * Z-INDEX SCALE
   * ============================================================ */
  --z-base:       0;
  --z-raised:     10;
  --z-dropdown:   100;
  --z-sticky:     200;
  --z-nav:        300;
  --z-overlay:    400;
  --z-modal:      500;
  --z-toast:      600;
  --z-tooltip:    700;

  /* ============================================================
   * ICONS & IMAGES
   * ============================================================ */
  --icon-size-sm:   16px;
  --icon-size-md:   24px;
  --icon-size-lg:   40px;
  --icon-size-xl:   64px;

  /* ============================================================
   * BOOKING CALENDAR — DATE STATE COLORS
   * ============================================================ */
  --calendar-available-bg:    var(--color-white);
  --calendar-available-color: var(--color-text-primary);
  --calendar-available-border: var(--color-grey-200);
  --calendar-booked-bg:       var(--color-grey-100);
  --calendar-booked-color:    var(--color-grey-400);
  --calendar-blocked-bg:      var(--color-error-bg);
  --calendar-blocked-color:   var(--color-error);
  --calendar-selected-bg:     var(--color-primary);
  --calendar-selected-color:  var(--color-white);
  --calendar-today-border:    var(--color-accent);

  /* ============================================================
   * FOCUS / ACCESSIBILITY
   * ============================================================ */
  --focus-ring-color:   var(--color-accent);
  --focus-ring-width:   3px;
  --focus-ring-offset:  2px;
  --min-touch-target:   44px;     /* Minimum touch target (WCAG) */
}
```

---

## base.css

```css
/**
 * base.css — Global reset and foundational styles
 * References design-tokens.css — NO raw values here.
 */

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 100%;
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}

body {
  font-family: var(--font-body);
  font-size: var(--text-base);
  font-weight: var(--weight-regular);
  line-height: var(--leading-normal);
  color: var(--color-text-primary);
  background-color: var(--color-bg-body);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ── Headings ── */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  font-weight: var(--weight-bold);
  line-height: var(--leading-tight);
  color: var(--color-text-primary);
}

h1 { font-size: var(--text-4xl); }
h2 { font-size: var(--text-3xl); }
h3 { font-size: var(--text-xl); }
h4 { font-size: var(--text-lg); }
h5 { font-size: var(--text-md); }
h6 { font-size: var(--text-base); }

/* ── Body text ── */
p {
  font-size: var(--text-base);
  line-height: var(--leading-relaxed);
  color: var(--color-text-secondary);
}

/* ── Links ── */
a {
  color: var(--color-text-link);
  text-decoration: none;
  transition: color var(--transition-fast);
}

a:hover {
  color: var(--color-primary-dark);
}

/* ── Images ── */
img, video {
  max-width: 100%;
  display: block;
}

/* ── Lists ── */
ul, ol {
  list-style: none;
}

/* ── Focus styles (accessibility) ── */
:focus-visible {
  outline: var(--focus-ring-width) solid var(--focus-ring-color);
  outline-offset: var(--focus-ring-offset);
  border-radius: var(--radius-sm);
}

/* ── Reduced motion ── */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## layout.css

```css
/**
 * layout.css — Container, grid, section wrappers
 * References design-tokens.css only.
 */

/* ── Container ── */
.container {
  width: 100%;
  max-width: var(--container-max);
  margin-inline: auto;
  padding-inline: var(--space-section-x);
}

.container--narrow {
  max-width: var(--container-narrow);
}

.container--wide {
  max-width: var(--container-wide);
}

/* ── Section wrapper ── */
.section {
  padding-block: var(--space-section-y);
}

.section--alt {
  background-color: var(--color-bg-alt);
}

.section--dark {
  background-color: var(--color-bg-dark);
  color: var(--color-text-on-dark);
}

.section--primary {
  background-color: var(--color-primary);
  color: var(--color-text-on-primary);
}

/* ── Section header ── */
.section-header {
  text-align: center;
  margin-bottom: var(--space-12);
}

.section-header h2 {
  margin-bottom: var(--space-4);
}

.section-header p {
  font-size: var(--text-lg);
  max-width: 600px;
  margin-inline: auto;
}

.section--dark .section-header h2,
.section--primary .section-header h2 {
  color: var(--color-text-on-dark);
}

.section--dark .section-header p,
.section--primary .section-header p {
  color: rgba(255, 255, 255, 0.75);
}

/* ── Grids ── */
.grid {
  display: grid;
  gap: var(--space-gap);
}

.grid--2 { grid-template-columns: repeat(2, 1fr); }
.grid--3 { grid-template-columns: repeat(3, 1fr); }
.grid--4 { grid-template-columns: repeat(4, 1fr); }

/* Responsive auto-fit grids */
.grid--auto-sm  { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.grid--auto-md  { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.grid--auto-lg  { grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); }

/* ── Flex helpers ── */
.flex        { display: flex; }
.flex-center { display: flex; align-items: center; justify-content: center; }
.flex-between { display: flex; align-items: center; justify-content: space-between; }
.flex-col    { display: flex; flex-direction: column; }
.flex-wrap   { flex-wrap: wrap; }
.gap-sm      { gap: var(--space-4); }
.gap-md      { gap: var(--space-6); }
.gap-lg      { gap: var(--space-8); }

/* Mobile: collapse grids */
@media (max-width: 767px) {
  .grid--2,
  .grid--3,
  .grid--4 { grid-template-columns: 1fr; }
}
```

---

## utilities.css

```css
/**
 * utilities.css — Reusable helper classes
 */

/* ── Screen-reader only (accessibility) ── */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* ── Text utilities ── */
.text-center { text-align: center; }
.text-left   { text-align: left; }
.text-right  { text-align: right; }
.text-primary-color { color: var(--color-primary); }
.text-accent-color  { color: var(--color-accent); }
.text-muted         { color: var(--color-text-muted); }
.text-on-dark       { color: var(--color-text-on-dark); }

/* ── Font weights ── */
.font-medium    { font-weight: var(--weight-medium); }
.font-semibold  { font-weight: var(--weight-semibold); }
.font-bold      { font-weight: var(--weight-bold); }

/* ── Spacing ── */
.mt-auto  { margin-top: auto; }
.mb-0     { margin-bottom: 0; }

/* ── Display ── */
.hidden         { display: none !important; }
.block          { display: block; }
.inline-flex    { display: inline-flex; }

/* Mobile only / Desktop only */
.mobile-only  { display: block; }
.desktop-only { display: none; }

@media (min-width: 768px) {
  .mobile-only  { display: none; }
  .desktop-only { display: block; }
}

/* ── Divider ── */
.divider {
  border: none;
  border-top: var(--border-width) solid var(--border-color);
  margin-block: var(--space-8);
}

/* ── Badge / Tag ── */
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  background: var(--color-primary-alpha-10);
  color: var(--color-primary);
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-wide);
  border-radius: var(--radius-full);
  text-transform: uppercase;
}

.badge--accent {
  background: var(--color-accent-dark);
  color: var(--color-white);
}

/* ── Icon circle wrapper ── */
.icon-circle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: var(--icon-size-xl);
  height: var(--icon-size-xl);
  background: var(--color-primary-alpha-10);
  color: var(--color-primary);
  border-radius: var(--radius-full);
}

.section--dark .icon-circle {
  background: rgba(255,255,255,0.10);
  color: var(--color-accent);
}
```

---

## How to Change a Brand Color

**Step 1:** Open `static/css/design-tokens.css`

**Step 2:** Find the token:
```css
/* Change just the HSL values for the primary color */
--brand-primary-h: 212;   /* ← Change hue here */
--brand-primary-s: 77%;   /* ← Change saturation here */
--brand-primary-l: 28%;   /* ← Change lightness here */
```

**Step 3:** Save. Done. The primary color updates across:
- Navigation
- All buttons
- All card hover effects
- Hero overlay tint
- Badge backgrounds
- Shadow colors
- Calendar selected state
- Sticky CTA background
- Footer links
- Form focus rings
- Icon accent colors
- Section backgrounds

**Example — Change to a green brand:**
```css
--brand-primary-h: 155;
--brand-primary-s: 80%;
--brand-primary-l: 28%;
```

**Example — Change to a warm orange brand:**
```css
--brand-primary-h: 24;
--brand-primary-s: 90%;
--brand-primary-l: 40%;
```

---

## How to Change the Font

**Step 1:** Add the new Google Font `<link>` to `base.html`

**Step 2:** Open `design-tokens.css` and update:
```css
--font-heading: 'Poppins', sans-serif;   /* ← Change here only */
--font-body:    'Poppins', sans-serif;   /* ← And here if same */
```

Done. Both heading and body fonts update everywhere.

---

## Component Pattern — Example: Card

Every component must follow this pattern — reference tokens, no raw values:

```css
/* components/cards.css */

.card {
  background: var(--color-bg-card);         /* ✅ token */
  border-radius: var(--radius-lg);           /* ✅ token */
  box-shadow: var(--shadow-md);              /* ✅ token */
  padding: var(--space-card);               /* ✅ token */
  border: var(--border-width) solid var(--border-color); /* ✅ token */
  transition: transform var(--transition-base),
              box-shadow var(--transition-base);
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-primary-md);      /* ✅ token */
}

.card__title {
  font-family: var(--font-heading);          /* ✅ token */
  font-size: var(--text-xl);                /* ✅ token */
  font-weight: var(--weight-semibold);      /* ✅ token */
  color: var(--color-text-primary);         /* ✅ token */
  margin-bottom: var(--space-2);            /* ✅ token */
}

/* ❌ DO NOT DO THIS: */
/* .card { background: #fff; border-radius: 20px; padding: 32px; } */
```

---

## CSS Naming Convention (BEM)

Use **BEM (Block Element Modifier)** naming:
```css
.block {}             /* Component block: .card, .nav, .hero */
.block__element {}    /* Child:           .card__title, .nav__logo */
.block--modifier {}   /* Variant:         .card--featured, .btn--large */
```

---

## Breakpoints (Mobile-First)

All media queries must be mobile-first (`min-width`):

```css
/* In layout.css — referenced as comments */
/* xs  : default (no query) — 320px+ */
/* sm  : @media (min-width: 480px) */
/* md  : @media (min-width: 768px) */
/* lg  : @media (min-width: 1024px) */
/* xl  : @media (min-width: 1280px) */
/* 2xl : @media (min-width: 1440px) */
```

```css
/* ✅ Correct — mobile first */
.grid { grid-template-columns: 1fr; }
@media (min-width: 768px) { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .grid { grid-template-columns: repeat(3, 1fr); } }

/* ❌ Wrong — desktop first */
.grid { grid-template-columns: repeat(3, 1fr); }
@media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }
```

---

## Related Documents
- [`27-landing-page-design-system.md`](./27-landing-page-design-system.md) — Color/typography values to use
- [`12-frontend-ux.md`](./12-frontend-ux.md) — UX principles
- [`26-ai-implementation-guide.md`](./26-ai-implementation-guide.md) — Implementation rules
