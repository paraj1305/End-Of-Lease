# 13 — SEO Requirements

## Overview
The website must be fully SEO-optimised to rank for local cleaning service searches in Australia. All important content must exist as crawlable HTML — video and JavaScript content alone does not satisfy SEO requirements.

---

## Page-Level SEO Requirements

### Home / Landing Page
| Element | Content |
|---------|---------|
| `<title>` | `Professional End of Lease Cleaning — [City] | [Brand Name]` |
| `<meta name="description">` | 150–160 char compelling description of the service, mentioning key city/suburb |
| `<h1>` | One only — the primary hero headline (e.g., "Professional End of Lease Cleaning in [City]") |
| `<h2>` | Section headings (packages, how it works, why choose us, etc.) |
| Canonical URL | `<link rel="canonical" href="https://domain.com.au/">` |
| Open Graph | `og:title`, `og:description`, `og:image`, `og:url`, `og:type` |
| Twitter Card | `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image` |

### Services / Packages Page
| Element | Content |
|---------|---------|
| `<title>` | `End of Lease Cleaning Packages — [City] | [Brand Name]` |
| `<meta name="description">` | Description of available packages |
| `<h1>` | "End of Lease Cleaning Packages" |
| Canonical | Page canonical URL |

### About Us Page
| Element | Content |
|---------|---------|
| `<title>` | `About Us — [Brand Name] | Professional Cleaners` |
| `<h1>` | "About [Brand Name]" |

### Contact Page
| Element | Content |
|---------|---------|
| `<title>` | `Contact Us — [Brand Name] | Book Your Cleaning` |
| `<h1>` | "Contact Us" |

### FAQ Page
| Element | Content |
|---------|---------|
| `<title>` | `FAQ — End of Lease Cleaning Questions Answered | [Brand Name]` |
| `<h1>` | "Frequently Asked Questions" |
| FAQ Schema | Required — see below |

---

## Structured Data (JSON-LD)

### LocalBusiness Schema (All pages — in `<head>` or before `</body>`)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Brand Name]",
  "description": "Professional end of lease cleaning service.",
  "url": "https://domain.com.au",
  "telephone": "[Phone number — confirmed by client]",
  "email": "[Email — confirmed by client]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Address — confirmed by client]",
    "addressLocality": "[City]",
    "addressRegion": "NSW",
    "postalCode": "[Postcode]",
    "addressCountry": "AU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[Lat]",
    "longitude": "[Lng]"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      "opens": "08:00",
      "closes": "18:00"
    }
  ],
  "priceRange": "$$",
  "image": "https://domain.com.au/static/images/og-image.jpg",
  "sameAs": []
}
```

### Service Schema (Services/Packages page)

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "End of Lease Cleaning",
  "provider": {
    "@type": "LocalBusiness",
    "name": "[Brand Name]"
  },
  "areaServed": {
    "@type": "State",
    "name": "New South Wales"
  },
  "description": "Professional end of lease cleaning services for 2–5 bedroom homes.",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "AUD",
    "price": "[Starting price — from admin]"
  }
}
```

### FAQ Schema (FAQ page and FAQ section on landing page)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is included in the end of lease cleaning?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer — confirmed by client]"
      }
    },
    {
      "@type": "Question",
      "name": "How does the booking work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer]"
      }
    }
  ]
}
```

---

## Sitemap

**URL:** `/sitemap.xml`

Use Django's `django.contrib.sitemaps` framework.

```python
# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticPagesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['home', 'services', 'about', 'contact', 'faq', 'booking']

    def location(self, item):
        return reverse(item)
```

Pages to include in sitemap:
- Home `/`
- Services/Packages `/services/`
- About `/about/`
- Contact `/contact/`
- FAQ `/faq/`
- Booking `/book/`

---

## robots.txt

**URL:** `/robots.txt`

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /webhooks/

Sitemap: https://domain.com.au/sitemap.xml
```

---

## Image SEO

- All `<img>` tags must have descriptive `alt` attributes
- Alt text must describe the image content (not keyword-stuffed)
- Images must use WebP format (with JPEG fallback via `<picture>` element)
- Images must have explicit `width` and `height` attributes to prevent CLS
- Images below the fold must use `loading="lazy"`
- Hero/above-fold images must NOT use lazy loading (preload instead)

```html
<!-- Hero image (above fold) -->
<link rel="preload" as="image" href="/static/images/hero-poster.webp">

<!-- Below-fold image -->
<picture>
  <source srcset="/static/images/clean-kitchen.webp" type="image/webp">
  <img src="/static/images/clean-kitchen.jpg" 
       alt="Professionally cleaned kitchen after end of lease cleaning"
       width="800" height="600"
       loading="lazy">
</picture>
```

---

## URL Structure

| Page | URL |
|------|-----|
| Home | `/` |
| Services | `/services/` |
| About | `/about/` |
| Contact | `/contact/` |
| FAQ | `/faq/` |
| Booking | `/book/` |
| Booking Step 1 | `/book/package/` |
| Booking Step 2 | `/book/addons/` |
| Booking Step 3 | `/book/datetime/` |
| Booking Step 4 | `/book/details/` |
| Booking Step 5 | `/book/review/` |
| Payment | `/book/payment/` |
| Confirmation | `/book/confirmation/<reference>/` |
| Privacy Policy | `/privacy/` |
| Terms | `/terms/` |
| Cancellation | `/cancellation-policy/` |

---

## Service Area SEO

- The landing page should include a dedicated "Areas We Serve" section
- Each suburb/city mentioned in crawlable HTML (not just in images or video)
- Link to individual suburb landing pages in Phase 2
- Example content: "We provide end of lease cleaning in [Suburb 1], [Suburb 2], [Suburb 3]..."

---

## Video SEO Considerations

- The hero video must NOT be the sole container of important SEO content
- All headline text, descriptions, and CTAs must exist as HTML elements
- Add `VideoObject` schema markup if appropriate
- Provide a `poster` image that is meaningful for the page

---

## Open Graph Image

- Size: 1200×630px
- Contains: brand logo, headline, visual of clean home
- Used when page is shared on social media (Facebook, LinkedIn, WhatsApp)
- Stored at `/static/images/og-image.jpg` and `/static/images/og-image.webp`

---

## Performance as SEO

Google uses Core Web Vitals as a ranking signal. See `11-pwa-requirements.md` for targets:
- LCP < 2.5s
- INP < 200ms
- CLS < 0.1

---

## Related Documents
- `01-project-overview.md`
- `11-pwa-requirements.md`
- `12-frontend-ux.md`
- `27-landing-page-design-system.md`
