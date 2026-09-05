"""
config/context_processors.py — Injects global business constants into all template contexts.
"""
from config import constants


def site_constants(request):
    return {
        'CALLBACK_ESTIMATE_MINUTES': constants.CALLBACK_ESTIMATE_MINUTES,
        'DEPOSIT_REQUIRED': constants.DEPOSIT_REQUIRED,
        'DEPOSIT_PERCENTAGE': constants.DEPOSIT_PERCENTAGE,
        'CONTACT_PHONE': constants.CONTACT_PHONE,
        'CONTACT_EMAIL': constants.CONTACT_EMAIL,
    }
