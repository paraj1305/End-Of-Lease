import os
from .base import *

DEBUG = False

_allowed_hosts = os.getenv('ALLOWED_HOSTS', '134.199.166.225,localhost,127.0.0.1')
ALLOWED_HOSTS = [h.strip() for h in _allowed_hosts.split(',') if h.strip()]
if '134.199.166.225' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('134.199.166.225')

_csrf_origins = os.getenv('CSRF_TRUSTED_ORIGINS', 'http://134.199.166.225,https://134.199.166.225')
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _csrf_origins.split(',') if o.strip()]
for _origin in ('http://134.199.166.225', 'https://134.199.166.225'):
    if _origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(_origin)

# Security settings
# Set to True when SSL certificate is configured on domain; defaults to False for raw IP access
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'False') == 'True'
SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', 'False') == 'True'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Email configuration
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
        'HOST': os.getenv('EMAIL_HOST'),
        'PORT': int(os.getenv('EMAIL_PORT', 587)),
        'USE_TLS': os.getenv('EMAIL_USE_TLS', 'True') == 'True',
        'USER': os.getenv('EMAIL_HOST_USER'),
        'PASSWORD': os.getenv('EMAIL_HOST_PASSWORD'),
    }
}
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
