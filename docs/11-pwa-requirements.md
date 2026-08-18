# 11 — PWA Requirements

## Overview
The platform must be installable as a Progressive Web App (PWA) on both iOS and Android devices. This gives the cleaning service an app-like experience without requiring a native app.

---

## PWA Goals

1. **Installable** — Customer can add the website to their home screen on iOS and Android
2. **Fast** — Pages load quickly even on slower connections
3. **Offline capable** — At minimum, show an offline fallback page
4. **App-like** — Full-screen experience after installation, without browser chrome

---

## Web App Manifest

**File:** `/static/manifest.json`

```json
{
  "name": "End of Lease Cleaning",
  "short_name": "EOL Cleaning",
  "description": "Professional end of lease cleaning service. Book online in minutes.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FFFFFF",
  "theme_color": "#1A1A2E",
  "orientation": "portrait",
  "icons": [
    {
      "src": "/static/icons/icon-72.png",
      "sizes": "72x72",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-96.png",
      "sizes": "96x96",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-128.png",
      "sizes": "128x128",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-144.png",
      "sizes": "144x144",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-152.png",
      "sizes": "152x152",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/static/icons/icon-384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable any"
    }
  ],
  "screenshots": [
    {
      "src": "/static/screenshots/home-mobile.png",
      "sizes": "390x844",
      "type": "image/png",
      "form_factor": "narrow"
    }
  ],
  "categories": ["lifestyle", "shopping"],
  "lang": "en-AU"
}
```

> **Note:** Replace `theme_color` and `background_color` with the client's final brand colors.

---

## HTML Link Tags (base template)

```html
<link rel="manifest" href="/static/manifest.json">
<meta name="theme-color" content="#1A1A2E">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="EOL Cleaning">
<link rel="apple-touch-icon" href="/static/icons/icon-192.png">
```

---

## Service Worker

**File:** `/static/sw.js`

### Cache Strategy
- **Cache-first** for static assets (CSS, JS, icons, fonts)
- **Network-first** for HTML pages (fresh content, fall back to cache)
- **Stale-while-revalidate** for API responses (calendar availability)

### Offline Fallback
- If a page cannot be fetched and is not cached, display `/offline.html`
- Offline page should be minimal and branded, explaining the user is offline

### Precached Assets
```javascript
const PRECACHE_URLS = [
  '/',
  '/offline.html',
  '/static/css/main.css',
  '/static/js/main.js',
  '/static/icons/icon-192.png',
];
```

### Service Worker Registration

```html
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/static/sw.js')
        .then(reg => console.log('SW registered:', reg.scope))
        .catch(err => console.error('SW registration failed:', err));
    });
  }
</script>
```

---

## Install Prompt (Android)

- Detect the `beforeinstallprompt` event
- Show a subtle "Add to Home Screen" banner after the user has browsed for a few seconds or completed a booking
- Do not show immediately on page load (non-intrusive)
- Banner should be dismissible

```javascript
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  // Show install banner UI
  showInstallBanner();
});
```

---

## iOS Considerations

- iOS does not support `beforeinstallprompt`
- Display an iOS install hint: "Tap Share → Add to Home Screen" in a subtle banner
- Show only once per session (use sessionStorage)
- Detect iOS with user-agent check: `navigator.userAgent.includes('iPhone')` or similar

---

## Performance Targets (Core Web Vitals)

| Metric | Target |
|--------|--------|
| LCP (Largest Contentful Paint) | < 2.5 seconds |
| INP (Interaction to Next Paint) | < 200 ms |
| CLS (Cumulative Layout Shift) | < 0.1 |
| FCP (First Contentful Paint) | < 1.8 seconds |
| TTFB (Time to First Byte) | < 600 ms |

---

## Mobile UX Requirements

- Minimum touch target size: 44×44px
- Font size minimum: 16px (to prevent iOS auto-zoom on form inputs)
- Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- No horizontal scroll at any screen width ≥ 320px
- Sticky "Book a Cleaning" CTA on mobile landing page
- Smooth scrolling: `scroll-behavior: smooth`

---

## Checklist for PWA Compliance

- [ ] `manifest.json` linked in HTML
- [ ] Service Worker registered
- [ ] HTTPS in production
- [ ] At least one 192×192 maskable icon
- [ ] At least one 512×512 icon
- [ ] `start_url` defined in manifest
- [ ] Offline fallback page exists
- [ ] `theme_color` set
- [ ] PWA audited with Lighthouse (target score ≥ 90)

---

## Related Documents
- `12-frontend-ux.md`
- `13-seo-requirements.md`
- `19-testing-requirements.md`
