"""
config/constants.py — Central source of truth for global business constants & SLAs.
Change any constant here and it automatically propagates across all templates, views, and emails.
"""

# Callback SLA in minutes for new booking confirmations
# Change this number (e.g. 5, 10) in one place to update all booking pages & confirmation screens.
CALLBACK_ESTIMATE_MINUTES = 15

# Upfront Deposit Policy (False = 0% deposit required, pay full on day of clean)
DEPOSIT_REQUIRED = False
DEPOSIT_PERCENTAGE = 0

# Support & Contact
CONTACT_PHONE = "02 7988 9050"
CONTACT_EMAIL = "hello@finalclean.com.au"
