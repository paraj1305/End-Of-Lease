import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
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
