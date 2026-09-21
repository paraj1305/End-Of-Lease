from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'testserver', '134.199.166.225', '*']

# Email testing backend
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}
