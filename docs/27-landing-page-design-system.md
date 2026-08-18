# 27 — Landing Page Design System

## Overview

This document defines the complete design system and section-by-section specification for the landing page. This is the primary conversion page of the website and must feel **premium, modern, fast, trustworthy, and visually impressive**.

### Design Inspiration
- **Primary UX reference:** [moveoutcleaning.au](https://moveoutcleaning.au/) — for overall experience, section flow, visual hierarchy, spacing, and premium cleaning-service feel.
- **Additional inspiration:** [sparkleclean.au](https://sparkleclean.au/)
- **Competitors studied:** exitcleaners.com.au, kleeningcrew.com.au, freshallseasons.com.au

> ⚠️ **IMPORTANT:** The design must be ORIGINAL. Do NOT copy logos, brand names, copyrighted images/video, exact text, or proprietary assets from any reference website. Use these only as quality benchmarks and structural inspiration.

---

## Design Principles

| Principle | Implementation |
|-----------|---------------|
| Premium | Sophisticated colors, generous whitespace, refined typography |
| Mobile-first | 375px default, scale up to 1440px |
| High-conversion | Clear CTAs, social proof, transparent pricing |
| Fast | Optimised video, lazy images, minimal JS |
| Trustworthy | Professional tone, trust signals, transparent pricing |
| Modern | Smooth animations, clean cards, contemporary layout |

---

## 1. Color System

> **⚠️ The client will provide final brand colors and logo before launch.**
> The following is a placeholder color system designed to feel premium for a cleaning service.
> All colors are defined as CSS custom properties so they can be updated with a single change.

```css
:root {
  /* ── Primary Brand Colors ── */
  /* Replace with client's brand colors */
  --color-primary: #0F4C81;          /* Deep professional blue */
  --color-primary-light: #1A6BA8;
  --color-primary-dark: #0A3560;
  
  /* ── Accent Colors ── */
  --color-accent: #00B4D8;           /* Fresh cyan — cleanliness */
  --color-accent-light: #90E0EF;
  --color-accent-dark: #0077B6;
  
  /* ── Neutrals ── */
  --color-white: #FFFFFF;
  --color-off-white: #F8F9FA;
  --color-light-grey: #EEF0F2;
  --color-mid-grey: #9CA3AF;
  --color-dark-grey: #374151;
  --color-near-black: #111827;
  
  /* ── Semantic Colors ── */
  --color-success: #059669;          /* Available date */
  --color-error: #DC2626;            /* Booked / blocked date */
  --color-warning: #D97706;
  
  /* ── Surface & Background ── */
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: #F8F9FA;
  --color-bg-dark: #0F1923;          /* Dark sections */
  --color-bg-hero-overlay: rgba(10, 20, 40, 0.55);  /* Hero video overlay */
  
  /* ── Text Colors ── */
  --color-text-primary: #111827;
  --color-text-secondary: #6B7280;
  --color-text-on-dark: #FFFFFF;
  --color-text-on-primary: #FFFFFF;
}
```

### Color Usage by Section
| Section | Background | Text |
|---------|-----------|------|
| Hero | Dark overlay over video | White |
| Trust/Value Props | Off-white | Near-black |
| How It Works | White | Near-black |
| Packages | Off-white | Near-black |
| Add-ons | White | Near-black |
| Before/After | Dark | White |
| Why Choose Us | Primary blue gradient | White |
| Testimonials | Off-white | Near-black |
| Service Areas | White | Near-black |
| FAQ | Off-white | Near-black |
| Final CTA | Primary blue | White |
| Footer | Near-black | White/Grey |

---

## 2. Typography

```css
:root {
  /* ── Font Families ── */
  --font-heading: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  
  /* ── Font Sizes (fluid/responsive) ── */
  --text-xs: clamp(0.75rem, 1.5vw, 0.875rem);     /* 12–14px */
  --text-sm: clamp(0.875rem, 1.5vw, 1rem);         /* 14–16px */
  --text-base: clamp(1rem, 2vw, 1.125rem);          /* 16–18px */
  --text-lg: clamp(1.125rem, 2.5vw, 1.25rem);      /* 18–20px */
  --text-xl: clamp(1.25rem, 3vw, 1.5rem);           /* 20–24px */
  --text-2xl: clamp(1.5rem, 4vw, 2rem);             /* 24–32px */
  --text-3xl: clamp(1.75rem, 5vw, 2.5rem);          /* 28–40px */
  --text-4xl: clamp(2rem, 6vw, 3.5rem);             /* 32–56px */
  --text-hero: clamp(2.25rem, 8vw, 5rem);            /* 36–80px — hero only */
  
  /* ── Font Weights ── */
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;
  --weight-extrabold: 800;
  
  /* ── Line Heights ── */
  --leading-tight: 1.2;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.65;
}
```

### Typography Scale Usage
| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Hero headline | `--text-hero` | 800 | All caps or Title Case |
| Section H2 | `--text-3xl` | 700 | |
| Card title | `--text-xl` | 600 | |
| Body copy | `--text-base` | 400 | |
| Captions/labels | `--text-sm` | 500 | |
| CTAs / buttons | `--text-base` | 600 | Letter-spacing: 0.5px |

**Google Font Import:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

---

## 3. Spacing System

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-32: 128px;
  
  /* Section padding */
  --section-padding-y: clamp(60px, 8vw, 120px);
  --section-padding-x: clamp(20px, 5vw, 80px);
  
  /* Container max width */
  --container-max: 1280px;
  --container-narrow: 760px;
}
```

---

## 4. Border Radius

```css
:root {
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-xl: 28px;
  --radius-full: 9999px;  /* Pills, tags */
}
```

---

## 5. Shadows

```css
:root {
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.10), 0 2px 6px rgba(0,0,0,0.06);
  --shadow-lg: 0 12px 40px rgba(0,0,0,0.14), 0 4px 12px rgba(0,0,0,0.08);
  --shadow-xl: 0 24px 60px rgba(0,0,0,0.18);
  --shadow-card-hover: 0 20px 50px rgba(15, 76, 129, 0.18);
  --shadow-cta: 0 8px 24px rgba(15, 76, 129, 0.40);
}
```

---

## 6. Buttons

```css
/* ── Primary CTA Button ── */
.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: 16px 36px;
  background: var(--color-primary);
  color: var(--color-text-on-primary);
  font-size: var(--text-base);
  font-weight: var(--weight-semibold);
  letter-spacing: 0.5px;
  border: none;
  border-radius: var(--radius-full);
  box-shadow: var(--shadow-cta);
  cursor: pointer;
  transition: transform 150ms ease-out, box-shadow 150ms ease-out, background 150ms;
  text-decoration: none;
}

.btn-primary:hover {
  background: var(--color-primary-light);
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(15, 76, 129, 0.50);
}

.btn-primary:active {
  transform: translateY(0);
}

/* ── Secondary/Ghost Button ── */
.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: 14px 32px;
  background: transparent;
  color: var(--color-white);
  font-size: var(--text-base);
  font-weight: var(--weight-medium);
  border: 2px solid rgba(255, 255, 255, 0.60);
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: background 150ms, border-color 150ms;
  text-decoration: none;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.10);
  border-color: rgba(255, 255, 255, 0.90);
}

/* ── Sticky Mobile CTA ── */
.sticky-mobile-cta {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 12px 24px;
  padding-bottom: calc(12px + env(safe-area-inset-bottom));
  background: var(--color-primary);
  box-shadow: 0 -4px 20px rgba(0,0,0,0.20);
  z-index: 100;
  display: none;  /* Shown via JS after hero scrolls out */
}

@media (max-width: 767px) {
  .sticky-mobile-cta {
    display: block;
  }
}
```

---

## 7. Cards

```css
.card {
  background: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  padding: var(--space-8);
  transition: transform 200ms ease-out, box-shadow 200ms ease-out;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card-hover);
}
```

---

## 8. Navigation

### Structure
```html
<nav class="site-nav" role="navigation" aria-label="Main navigation">
  <div class="nav-container">
    <a href="/" class="nav-logo" aria-label="Home">
      <img src="/static/images/logo.svg" alt="[Brand Name] Logo" width="160" height="40">
    </a>
    
    <ul class="nav-links" role="list">
      <li><a href="/services/">Services</a></li>
      <li><a href="/about/">About</a></li>
      <li><a href="/faq/">FAQ</a></li>
      <li><a href="/contact/">Contact</a></li>
    </ul>
    
    <a href="/book/" class="btn-primary nav-cta" id="nav-book-btn">
      Book a Cleaning
    </a>
    
    <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false">
      <!-- Hamburger icon -->
    </button>
  </div>
</nav>
```

### Behaviour
- **Transparent** when overlapping hero video
- **Solid** (`var(--color-bg-dark)` with `backdrop-filter: blur(12px)`) after scrolling past hero
- **Fixed / sticky** — stays at top of viewport
- **Mobile:** Hamburger button reveals a full-screen or slide-in drawer

---

## 9. Section-by-Section Specification

---

### SECTION 1 — HERO

**Purpose:** Immediate visual impact, communicate value, drive to booking CTA.

**Background:** Full-viewport-height video (cleaning transformation dirty→clean) with dark overlay.

**Layout:**
```
┌──────────────────────────────────────────────────┐
│                    [NAV]                          │
│                                                   │
│          [Full-screen background video]           │
│               [dark overlay ~55%]                 │
│                                                   │
│          From Messy to Perfectly Fresh            │
│    Professional End of Lease Cleaning, Made       │
│              Incredibly Simple.                   │
│                                                   │
│    [BOOK A CLEANING]    [VIEW SERVICES]           │
│                                                   │
│  ✓ 10% Deposit  ✓ Fast Booking  ✓ No Login      │
│                                                   │
│          ↓ Scroll to see the transformation       │
└──────────────────────────────────────────────────┘
```

**HTML structure:**

```html
<section class="hero" id="hero" aria-label="Hero — Professional cleaning service">
  <div class="hero-video-wrapper">
    <video
      id="hero-video"
      class="hero-video"
      preload="auto"
      muted
      playsinline
      aria-hidden="true"
      poster="/static/images/hero-poster.webp"
    >
      <source src="/static/video/hero.webm" type="video/webm">
      <source src="/static/video/hero.mp4" type="video/mp4">
    </video>
    <div class="hero-overlay" aria-hidden="true"></div>
  </div>
  
  <div class="hero-content">
    <h1 class="hero-headline">From Messy to<br> Perfectly Fresh</h1>
    <p class="hero-subheading">
      Professional End of Lease Cleaning, Made Incredibly Simple.
    </p>
    <div class="hero-ctas">
      <a href="/book/" class="btn-primary" id="hero-book-btn">
        Book a Cleaning
      </a>
      <a href="/services/" class="btn-secondary" id="hero-services-btn">
        View Services
      </a>
    </div>
    <ul class="hero-trust-pills" aria-label="Key trust points">
      <li>✓ 10% Deposit</li>
      <li>✓ Fast Online Booking</li>
      <li>✓ No Account Needed</li>
    </ul>
  </div>
  
  <div class="hero-scroll-hint" aria-hidden="true">
    <span>Scroll to see the transformation</span>
    <div class="scroll-arrow"></div>
  </div>
</section>
```

#### 9.1.1 Scroll-Driven Video Interaction

**Concept:** As the user scrolls through the hero section, the video plays forward. At 0% scroll = dirty room. At 100% scroll = clean room. The video represents the cleaning transformation.

**Implementation Strategy:**

```javascript
// static/js/scroll-video.js

(function() {
  'use strict';
  
  // Check if scroll video should be enabled
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isSaveData = navigator.connection?.saveData === true;
  const isSlowConnection = ['slow-2g', '2g'].includes(navigator.connection?.effectiveType);
  const isMobileSmall = window.innerWidth < 768;
  
  const video = document.getElementById('hero-video');
  if (!video) return;
  
  // ── FALLBACK MODE ──
  // If reduced motion, save-data, slow connection, or small mobile:
  // Use autoplay loop instead of scroll-driven
  if (prefersReducedMotion || isSaveData || isSlowConnection) {
    video.setAttribute('autoplay', '');
    video.setAttribute('loop', '');
    video.play().catch(() => {});
    return;
  }
  
  // ── SCROLL-DRIVEN MODE ──
  let ticking = false;
  const heroSection = document.getElementById('hero');
  
  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(updateVideo);
      ticking = true;
    }
  }
  
  function updateVideo() {
    ticking = false;
    if (!video.duration) return;
    
    const rect = heroSection.getBoundingClientRect();
    const scrollProgress = Math.max(0, Math.min(1,
      -rect.top / (rect.height - window.innerHeight)
    ));
    
    video.currentTime = scrollProgress * video.duration;
  }
  
  // Wait for video metadata to load before enabling scroll control
  video.addEventListener('loadedmetadata', () => {
    window.addEventListener('scroll', onScroll, { passive: true });
    updateVideo();
  });
  
  // Fallback: if video fails to load, show poster image gracefully
  video.addEventListener('error', () => {
    video.closest('.hero-video-wrapper').classList.add('video-failed');
  });
  
})();
```

**Mobile Fallback Behaviour:**
- On mobile < 768px: Use autoplay + loop by default (not scroll-driven)
- The short loop video shows the transformation repeatedly
- OR use a CSS before/after split image as a fallback
- The `prefers-reduced-motion` fallback applies universally regardless of screen size

**Performance Requirements:**
- Video must have `preload="auto"` for scroll scrubbing (metadata alone is insufficient)
- Provide a mobile-optimised lower-res version (optional: use `<source media>`)
- Poster image must load fast (< 200 KB WebP) — shown during video load
- If video load fails, poster image remains as hero background

#### 9.1.2 Hero Scroll Indicator
- Animated downward-scrolling arrow icon
- Disappears after user starts scrolling
- Hidden if `prefers-reduced-motion`

---

### SECTION 2 — TRUST / VALUE PROPOSITION

**Purpose:** Immediately communicate why this cleaning service is the right choice.

**Layout:** Row of 4–6 icon + text cards. Horizontal scroll on mobile, grid on desktop.

**Trust Signals:**
| Icon | Title | Subtitle |
|------|-------|---------|
| 🏅 | Professional Cleaners | Experienced, vetted, and trusted |
| 📱 | Easy Online Booking | Book in minutes, no account needed |
| ✅ | Reliable Service | We show up, on time, every time |
| 💰 | Transparent Pricing | No hidden fees. Pay 10% today |
| 🗓️ | Flexible Scheduling | Choose a date that works for you |
| ⭐ | Quality Guaranteed | We're not done until it's perfect |

**Design:** Clean white cards, subtle shadow, icon in brand primary color, 2–3 word title, short subtitle.

---

### SECTION 3 — HOW IT WORKS (SIMPLE BOOKING EXPERIENCE)

**Purpose:** Show customers how fast and easy booking is.

**Layout:** Numbered step list with icons. Horizontal on desktop, vertical on mobile.

**Steps:**
```
01  Choose Your Home
    Select the size that fits your property

02  Add Extra Services
    Optionally add garden, garage, or more

03  Pick a Date & Time
    See available dates instantly

04  Enter Your Details
    Just your name, phone, email & address

05  Pay 10% Deposit
    Secure your booking with a small deposit

06  Relax — We're On Our Way!
    We handle everything from here
```

**CTA:** "BOOK NOW — IT'S THAT SIMPLE" button after the steps.

---

### SECTION 4 — CLEANING PACKAGES

**Purpose:** Display available packages and convert to booking.

**Data source:** Django admin (CleaningPackage model) — fully dynamic.

**Layout:** 2-column grid on desktop, 1-column on mobile. Potentially horizontal scroll carousel on mobile.

**Package Card Design:**
```
┌─────────────────────────────────────┐
│  MOST POPULAR  ← (optional badge)   │
│                                     │
│  3 BHK End of Lease Cleaning       │
│  ~85–110 m²                         │
│                                     │
│  FROM                               │
│  $350                               │
│                                     │
│  ✓ All rooms vacuumed & mopped      │
│  ✓ Kitchen deep clean               │
│  ✓ Bathrooms scrubbed               │
│  ✓ Windows inside                   │
│  ✓ Skirting boards & switches       │
│  + 3 more included                  │
│                                     │
│  [BOOK THIS PACKAGE]                │
└─────────────────────────────────────┘
```

**Django Template:**
```html
{% for package in packages %}
<article class="package-card" id="package-{{ package.pk }}">
  <div class="package-card-header">
    <h3 class="package-name">{{ package.name }}</h3>
    <p class="package-area">{{ package.approximate_area }}</p>
    <div class="package-price">
      <span class="price-from">From</span>
      <span class="price-amount">${{ package.base_price }}</span>
    </div>
  </div>
  <ul class="package-includes">
    {% for item in package.included_services|slice:":5" %}
    <li>✓ {{ item }}</li>
    {% endfor %}
    {% if package.included_services|length > 5 %}
    <li class="more-items">+ {{ package.included_services|length|add:"-5" }} more included</li>
    {% endif %}
  </ul>
  <a href="/book/?package={{ package.pk }}" class="btn-primary package-cta">
    Book This Package
  </a>
</article>
{% endfor %}
```

---

### SECTION 5 — ADD-ON SERVICES

**Purpose:** Increase average order value and show service flexibility.

**Data source:** Django admin (AddOnService model) — fully dynamic.

**Layout:** Grid of add-on cards. 3 columns on desktop, 2 on tablet, 1 on mobile.

**Add-on Card Design:**
```
┌────────────────────────────────────┐
│  [Icon]                            │
│  Garden Cleaning                   │
│  Professional tidying of outdoor   │
│  garden and lawn areas.            │
│                                    │
│  + $XX.00                          │
│                          [ADD +]   │
└────────────────────────────────────┘
```

**Note:** Add-on selection on the landing page should pre-select the add-on in the booking flow, not interrupt the page (link to `/book/?addon=X` or open booking modal).

---

### SECTION 6 — BEFORE / AFTER

**Purpose:** Visual proof of the cleaning transformation. Build trust through results.

**Implementation Options:**
1. **Image Slider (Recommended for MVP):** A horizontal drag slider reveals the "After" image over the "Before" image. Pure CSS + minimal JS.
2. **Side-by-side images:** Simpler fallback.
3. **Scroll-driven split:** More complex, phase 2.

**Recommended: Image Comparison Slider**

```html
<section class="before-after-section" aria-labelledby="before-after-heading">
  <h2 id="before-after-heading">See the Difference We Make</h2>
  <p>Real transformations from our professional cleaning team.</p>
  
  <div class="before-after-slider" 
       role="img" 
       aria-label="Before and after cleaning comparison">
    <div class="before-image-wrapper">
      <picture>
        <source srcset="/static/images/before-kitchen.webp" type="image/webp">
        <img src="/static/images/before-kitchen.jpg" 
             alt="Kitchen before professional cleaning" 
             width="800" height="600"
             loading="lazy">
      </picture>
      <span class="image-label before-label">Before</span>
    </div>
    <div class="after-image-wrapper">
      <picture>
        <source srcset="/static/images/after-kitchen.webp" type="image/webp">
        <img src="/static/images/after-kitchen.jpg" 
             alt="Kitchen after professional cleaning"
             width="800" height="600"
             loading="lazy">
      </picture>
      <span class="image-label after-label">After</span>
    </div>
    <div class="slider-handle" aria-hidden="true">
      <div class="slider-line"></div>
      <div class="slider-circle">
        <svg><!-- left/right arrows icon --></svg>
      </div>
    </div>
  </div>
  
  <!-- Optional: multiple room comparisons as a carousel -->
</section>
```

**Label flexibility:** The "Before" and "After" labels are editable in the template. The client may want different language (e.g., "Move-out Day" / "After Our Cleaning").

**JavaScript:**

```javascript
// static/js/before-after-slider.js
// Implements touch and mouse drag on .before-after-slider
// Sets clip-path or width of the .after-image-wrapper based on drag position
// Accessible: role=slider, aria-valuenow on handle
```

---

### SECTION 7 — WHY CHOOSE US

**Purpose:** Reinforce trust and differentiation from competitors.

**Layout:** Grid of benefit cards. Dark background section for visual contrast.

**Benefits:**
| Icon | Title | Description |
|------|-------|-------------|
| 🧹 | Experienced Professionals | Fully trained and experienced cleaners |
| 🔒 | Bond-Back Guarantee | We clean to real estate agent standards |
| 📋 | Full Cleaning Checklist | Every item on the checklist, completed |
| 💳 | Pay Only 10% Today | Small deposit secures your date |
| ⚡ | Fast Online Booking | Book in under 3 minutes |
| 📞 | Dedicated Support | We're here if you need us |

---

### SECTION 8 — CUSTOMER REVIEWS

**Purpose:** Social proof through testimonials.

**MVP Approach:** Placeholder testimonials clearly marked. Use realistic-looking placeholder cards without real names.

**Layout:** 3-column grid on desktop. Horizontal scroll carousel on mobile.

**Testimonial Card Design:**
```
┌────────────────────────────────────────────────┐
│  ★★★★★                                          │
│                                                │
│  "The team did an incredible job — our        │
│  landlord was absolutely happy and we got     │
│  our full bond back without any issues!"      │
│                                               │
│  [Avatar]  J. S.                              │
│            Sydney, NSW                        │
└────────────────────────────────────────────────┘
```

> ⚠️ **Do NOT use real names or fabricate real reviews.** Use placeholder initials (J.S., M.K.) until the client provides real testimonials.

**Phase 2:** Testimonials managed from Django admin panel (model + admin CRUD).

---

### SECTION 9 — SERVICE AREAS

**Purpose:** SEO-friendly section communicating which areas are served.

**MVP Content:** Placeholder suburb list — client must provide final list.

**SEO requirement:** All suburb names must be in crawlable HTML text, not just in images.

**Layout:**
```html
<section class="service-areas" aria-labelledby="service-areas-heading">
  <h2 id="service-areas-heading">We Clean Across [City/Region]</h2>
  <p>Professional end of lease cleaning available in:</p>
  
  <ul class="area-tags" role="list">
    <!-- Client to provide final list -->
    <li>Parramatta</li>
    <li>Penrith</li>
    <li>Blacktown</li>
    <li>Liverpool</li>
    <!-- ... -->
    <li class="placeholder-note">[Add your suburb — Contact us]</li>
  </ul>
  
  <p>Don't see your area? <a href="/contact/">Contact us</a> — we may still be able to help.</p>
</section>
```

---

### SECTION 10 — FAQ

**Purpose:** Reduce friction by answering the most common questions before the customer asks.

**Layout:** Accordion/expandable list. 1-column on all screen sizes.

**Default FAQ Items:**

| Question | Answer Note |
|----------|-------------|
| What is included in the end of lease cleaning? | List all included items — confirm with client |
| How does online booking work? | Explain the 5-step process briefly |
| How much is the deposit? | "Only 10% of the total price is paid today. The remaining amount is paid on the day of cleaning." |
| Can I cancel my booking? | Link to cancellation policy — confirm policy with client |
| What if I need to change the date? | Reschedule policy — confirm with client |
| Do I need to provide cleaning supplies? | No — our team brings everything — confirm with client |
| How long does cleaning take? | Depends on property size — confirm average times with client |
| Do you offer a bond-back guarantee? | Confirm with client |

> All FAQ answers must be confirmed by the client before launch.

**FAQ Schema:** Add FAQPage JSON-LD schema markup for all FAQ items (see `13-seo-requirements.md`).

---

### SECTION 11 — FINAL CTA

**Purpose:** Last chance to convert. Strong, simple, direct.

**Design:** Full-width section in brand primary blue with white text.

```html
<section class="final-cta" aria-labelledby="final-cta-heading">
  <div class="final-cta-content">
    <h2 id="final-cta-heading">Ready for a Cleaner Home?</h2>
    <p>Book your professional end of lease cleaning today.<br>
       Simple. Fast. Reliable.</p>
    <a href="/book/" class="btn-cta-large" id="final-cta-btn">
      Book Your Cleaning
    </a>
    <p class="final-cta-sub">
      Only 10% deposit today &middot; No account required &middot; Easy online booking
    </p>
  </div>
</section>
```

---

### SECTION 12 — FOOTER

**Layout:** 4-column grid on desktop, 2-column on tablet, 1-column on mobile.

**Columns:**
1. **Logo + tagline + social links**
2. **Services** — links to packages/services
3. **Company** — About, FAQ, Contact, Areas
4. **Legal** — Privacy Policy, Terms, Cancellation Policy

**Bottom bar:** Copyright © [Year] [Brand Name] | ABN: [If provided by client]

```html
<footer class="site-footer" role="contentinfo">
  <div class="footer-grid">
    <div class="footer-brand">
      <img src="/static/images/logo-white.svg" alt="[Brand Name]" width="140" height="36">
      <p>Professional end of lease cleaning, made simple.</p>
      <!-- Social links if provided by client -->
    </div>
    <div class="footer-col">
      <h3>Services</h3>
      <ul>
        <li><a href="/services/">All Services</a></li>
        <li><a href="/services/#2bhk">2 BHK Cleaning</a></li>
        <!-- Dynamic from packages -->
      </ul>
    </div>
    <div class="footer-col">
      <h3>Company</h3>
      <ul>
        <li><a href="/about/">About Us</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h3>Legal</h3>
      <ul>
        <li><a href="/privacy/">Privacy Policy</a></li>
        <li><a href="/terms/">Terms of Service</a></li>
        <li><a href="/cancellation-policy/">Cancellation Policy</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>© {% now "Y" %} [Brand Name]. All rights reserved.</p>
  </div>
</footer>
```

---

## 10. Responsive Behaviour Summary

| Section | Mobile (< 768px) | Tablet (768–1023px) | Desktop (≥ 1024px) |
|---------|-----------------|--------------------|--------------------|
| Hero | Full-height, autoplay loop video | Full-height, scroll-driven | Full-height, scroll-driven |
| Trust | Horizontal scroll cards | 3-col grid | 6-col row |
| How It Works | Vertical numbered list | 3-col grid | 6-col horizontal |
| Packages | Single column | 2-col grid | 3–4 col grid or horizontal scroll |
| Add-ons | Single column | 2-col grid | 3-col grid |
| Before/After | Full-width slider | Full-width slider | Contained slider |
| Why Choose Us | 2-col grid | 3-col grid | 3-col grid |
| Testimonials | Horizontal scroll carousel | 2-col grid | 3-col grid |
| Service Areas | Wrapped tag cloud | Wrapped tag cloud | Wrapped tag cloud |
| FAQ | Full-width accordion | Full-width accordion | Contained accordion |
| Final CTA | Centered, full-width button | Centered | Centered |
| Footer | Single column | 2-col grid | 4-col grid |

---

## 11. Animation Summary

| Section | Animation | Disabled for reduced-motion |
|---------|-----------|--------------------------|
| Hero video | Scroll-driven → loop fallback | Static poster image |
| Hero text | Fade-in + translate-Y on load | No animation |
| Section entries | Fade-in via IntersectionObserver | No animation |
| Package cards | Staggered fade-in | No animation |
| Package card hover | Lift + shadow | No animation |
| Add-on card | Toggle border + checkmark | No animation |
| Before/after slider | Smooth clip-path drag | Instant snap |
| FAQ accordion | Height animate on open/close | Instant open/close |
| CTA button hover | Scale + shadow | No animation |
| Scroll hint arrow | Bounce animation | No animation |
| Sticky mobile CTA | Slide-up on appear | Instant appear |

---

## 12. Accessibility Requirements

- All images: descriptive `alt` text
- Video: `aria-hidden="true"` (decorative), poster image visible to screen readers
- Heading hierarchy: H1 in hero → H2 per section → H3 in cards
- Before/after slider: `role="img"` with `aria-label`, or `role="slider"` with `aria-valuenow`
- FAQ accordion: `aria-expanded`, `aria-controls`, keyboard navigation
- Color contrast: minimum 4.5:1 for all text (WCAG AA)
- Focus styles: visible on all interactive elements
- Sticky CTA: has accessible label ("Book a Cleaning")
- `prefers-reduced-motion`: all animations disabled when enabled

---

## 13. Page Load Order

For optimal performance and perceived speed:

1. **Immediately:** Base HTML, inline critical CSS for nav and hero
2. **Async:** Load full CSS file
3. **Preload:** Hero poster image (`<link rel="preload">`)
4. **Defer:** All JavaScript
5. **Lazy load:** All below-fold images, add-on section, testimonials
6. **Background:** Service worker registration

---

## 14. File Checklist for Landing Page

| File | Purpose |
|------|---------|
| `templates/public/home.html` | Landing page template |
| `static/css/landing.css` | Landing page styles |
| `static/js/scroll-video.js` | Scroll-driven video controller |
| `static/js/before-after-slider.js` | Before/after image slider |
| `static/js/main.js` | Nav, scroll events, sticky CTA, animations |
| `static/video/hero-transformation.mp4` | PLACEHOLDER hero video |
| `static/video/hero-transformation.webm` | PLACEHOLDER hero video (WebM) |
| `static/images/hero-poster.webp` | Hero video poster image |
| `static/images/before-*.webp` | PLACEHOLDER before photos |
| `static/images/after-*.webp` | PLACEHOLDER after photos |

---

## Related Documents
- `12-frontend-ux.md`
- `13-seo-requirements.md`
- `21-performance-strategy.md`
- `11-pwa-requirements.md`
- `20-content-strategy.md`
