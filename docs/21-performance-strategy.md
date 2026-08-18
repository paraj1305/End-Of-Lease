# 21 — Performance Strategy

## Overview
Performance is critical for this platform because:
1. The hero section uses a large video asset
2. Mobile users may be on slower connections
3. Core Web Vitals directly affect Google search rankings

---

## Video Performance

### Hero Video Requirements
| Property | Specification |
|---------|--------------|
| Format | MP4 (H.264) primary + WebM (VP9) fallback |
| Resolution | 1920×1080 for desktop, 854×480 for mobile |
| Duration | 30–60 sec (scroll-driven) OR 10–15 sec (loop) |
| Bitrate | 1–3 Mbps (compressed for web) |
| File size | < 10 MB desktop, < 5 MB mobile |
| Audio | Muted (no audio track needed) |
| Poster | WebP, 1920×1080, < 200 KB |

### Video HTML Pattern

```html
<video
  id="hero-video"
  class="hero-video"
  preload="metadata"
  muted
  playsinline
  poster="/static/images/hero-poster.webp"
  aria-label="Cleaning transformation video"
>
  <source src="/static/video/hero.webm" type="video/webm">
  <source src="/static/video/hero.mp4" type="video/mp4">
  <!-- Fallback: poster image is shown if video fails to load -->
</video>
```

### Scroll-Driven Video Strategy

For scroll-driven video playback:
- Use `video.currentTime` manipulation (not CSS animations) for frame-accurate control
- Video must be fully `preload="auto"` for smooth scrubbing
- Use `IntersectionObserver` to only activate scrubbing when video is in viewport
- Throttle scroll handler to ~60fps using `requestAnimationFrame`
- On low-end devices / slow connections: fall back to autoplay loop

### Mobile Video Fallback

Detect conditions for fallback:
```javascript
const shouldFallback = (
  window.matchMedia('(prefers-reduced-motion: reduce)').matches ||
  navigator.connection?.effectiveType === '2g' ||
  navigator.connection?.saveData === true ||
  window.innerWidth < 768  // Optional: mobile always uses loop
);
```

Fallback behavior:
- Remove scroll-driven behavior
- Play video as autoplay, muted, looped short clip (10–15 sec)
- OR: show static before/after split image

---

## Image Performance

### Format Strategy
- **WebP** as primary format (supported in all modern browsers)
- **JPEG/PNG** as fallback via `<picture>` element
- Consider **AVIF** for supported browsers (Phase 2)

### Image Pattern

```html
<picture>
  <source srcset="/static/images/clean-room.webp" type="image/webp">
  <img 
    src="/static/images/clean-room.jpg"
    alt="Professionally cleaned living room"
    width="800"
    height="600"
    loading="lazy"
    decoding="async"
  >
</picture>
```

### Above-Fold Images
- Hero poster: preload with `<link rel="preload">`
- No lazy loading on above-fold images

### Below-Fold Images
- All use `loading="lazy"` and `decoding="async"`
- Explicit `width` and `height` to prevent layout shift (CLS)

---

## CSS Performance

- Single compiled CSS file (`main.css`)
- No render-blocking CSS in `<head>` beyond the main stylesheet
- Inline critical CSS for above-fold content (Phase 2 optimisation)
- Use CSS custom properties (variables) — no CSS-in-JS

---

## JavaScript Performance

- Minimal JavaScript footprint
- HTMX for partial page updates (avoids full page reloads, smaller than a SPA framework)
- Vanilla JS for scroll animation and before/after slider
- No jQuery
- No heavy animation libraries (no GSAP, no Framer Motion)
- All JS deferred: `<script defer src="..."></script>`
- Avoid long tasks that block the main thread

---

## Font Loading

```html
<!-- Preconnect to Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Load font with display=swap to prevent FOIT -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

Alternatively: self-host font files for better performance (Phase 2).

---

## Caching Strategy

| Asset Type | Cache Duration |
|-----------|---------------|
| Static files (CSS, JS, images) | 1 year (cache-busting via content hash) |
| HTML pages | No cache / short cache |
| API responses (availability) | 1–5 minutes |
| Service Worker assets | Cache-first |

---

## Core Web Vitals Targets

| Metric | Target | Method |
|--------|--------|--------|
| LCP | < 2.5s | Preload hero poster, optimised video |
| INP | < 200ms | Minimal JS, no heavy libraries |
| CLS | < 0.1 | Explicit image dimensions, no late-loading content that shifts layout |
| FCP | < 1.8s | Server-side rendering, fast TTFB |
| TTFB | < 600ms | Efficient Django views, database queries optimised |

---

## Monitoring

- Use Google Search Console to monitor Core Web Vitals in production
- Run Lighthouse in Chrome DevTools before each major release
- Measure with WebPageTest.org for real-world network conditions

---

## Related Documents
- `11-pwa-requirements.md`
- `13-seo-requirements.md`
- `27-landing-page-design-system.md`
