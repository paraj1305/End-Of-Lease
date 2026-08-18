# 18 — Deployment & Hosting

## Overview
This document covers production deployment requirements for the Django application.

---

## Recommended Hosting Options

| Option | Pros | Cons |
|--------|------|------|
| **Railway** | Easy Django deploy, managed PostgreSQL, free SSL | Monthly cost |
| **Render** | Similar to Railway, free tier available | Cold starts on free tier |
| **DigitalOcean App Platform** | Reliable, scalable | More setup |
| **VPS (Ubuntu + Nginx + Gunicorn)** | Full control, cheapest at scale | Manual setup |

> **Recommended for MVP:** Railway or Render for simplicity.

---

## Production Requirements

- HTTPS (SSL certificate — mandatory for Stripe and PWA)
- PostgreSQL database (not SQLite in production)
- Static files served via WhiteNoise or CDN
- Environment variables managed securely (platform secrets or `.env`)
- Stripe webhook endpoint publicly accessible with correct URL configured in Stripe Dashboard
- Email SMTP configured

---

## Stripe Webhook Configuration

In Stripe Dashboard → Developers → Webhooks:
- Add endpoint: `https://yourdomain.com.au/webhooks/stripe/`
- Events to listen for: `payment_intent.succeeded`, `payment_intent.payment_failed`
- Copy the webhook signing secret to `STRIPE_WEBHOOK_SECRET` env var

---

## Gunicorn / WSGI

```bash
# Procfile (for Railway/Render/Heroku-style)
web: gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 2
```

---

## Static Files (WhiteNoise)

```python
# settings/production.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

## Database Migration on Deploy

```bash
python manage.py migrate
python manage.py collectstatic --no-input
```

---

## Cron Jobs

| Command | Schedule | Purpose |
|---------|---------|---------|
| `cleanup_draft_bookings` | Every hour | Remove stale draft bookings |

Set up via Railway/Render cron jobs or a simple scheduled task.

---

## Related Documents
- `15-django-project-structure.md`
- `09-payments.md`
