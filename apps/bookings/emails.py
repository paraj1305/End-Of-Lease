"""
Booking email notifications.

Sends two emails when a booking is confirmed:
  1. Confirmation email → customer
  2. Notification email → BOOKING_NOTIFICATION_EMAIL (set in .env)
"""

from django.core.mail import send_mail
from django.conf import settings
from config import constants


def _get_from_email():
    """Retrieve DEFAULT_FROM_EMAIL from MAILERS (Django 6.1) or settings fallback."""
    mailers = getattr(settings, 'MAILERS', {})
    default_mailer = mailers.get('default', {})
    return default_mailer.get(
        'DEFAULT_FROM_EMAIL',
        getattr(settings, 'DEFAULT_FROM_EMAIL', 'Final Clean <noreply@finalclean.com.au>')
    )


def send_booking_confirmation(booking):
    """
    Send a confirmation email to the customer and a notification to the
    admin/owner address defined in settings.BOOKING_NOTIFICATION_EMAIL.
    """
    _send_customer_confirmation(booking)
    _send_admin_notification(booking)


# ─────────────────────────────────────────────────
# Internal helpers
# ─────────────────────────────────────────────────

def _format_address(booking):
    return (
        f"{booking.service_address_street}, "
        f"{booking.service_address_suburb} "
        f"{booking.service_address_postcode} "
        f"{booking.service_address_state}"
    )


def _send_customer_confirmation(booking):
    """Email sent to the customer after their booking is confirmed."""
    subject = f"✅ Booking Confirmed — {booking.reference} | Final Clean"

    body = f"""Hi {booking.customer_name},

Your end-of-lease clean is booked! Here are your details:

  Booking Reference : {booking.reference}
  Date              : {booking.booking_date.strftime('%A, %d %B %Y')}
  Time Slot         : {booking.time_slot}
  Address           : {_format_address(booking)}

  Bedrooms          : {booking.bedrooms}
  Bathrooms         : {booking.bathrooms}
  Living Areas      : {booking.living_areas}
  Balconies         : {booking.balconies}

  Total Price       : ${booking.subtotal:.2f} inc. GST

What happens next?
  • Our team will call you within {constants.CALLBACK_ESTIMATE_MINUTES} minutes to confirm details.
  • You'll receive a 72-hour free re-clean guarantee.
  • Before & after photos are included with every clean.

If you have questions, reply to this email or call us on {constants.CONTACT_PHONE}.

Thanks for choosing Final Clean!
— The Final Clean Team
"""

    send_mail(
        subject=subject,
        message=body,
        from_email=_get_from_email(),
        recipient_list=[booking.customer_email],
        fail_silently=False,
    )


def _send_admin_notification(booking):
    """Email sent to the owner/admin when a new booking is confirmed."""
    admin_email = getattr(settings, 'BOOKING_NOTIFICATION_EMAIL', settings.ADMIN_EMAIL)

    subject = f"🆕 New Booking — {booking.reference} | {booking.customer_name}"

    body = f"""New booking confirmed!

──────────────────────────────
BOOKING REFERENCE : {booking.reference}
STATUS            : {booking.status.upper()}
──────────────────────────────

CUSTOMER DETAILS
  Name    : {booking.customer_name}
  Email   : {booking.customer_email}
  Phone   : {booking.customer_phone}

SERVICE ADDRESS
  {_format_address(booking)}

CLEAN DETAILS
  Date      : {booking.booking_date.strftime('%A, %d %B %Y')}
  Time Slot : {booking.time_slot}
  Bedrooms  : {booking.bedrooms}
  Bathrooms : {booking.bathrooms}
  Living    : {booking.living_areas}
  Balconies : {booking.balconies}

PRICING
  Base Clean   : ${booking.base_clean_price:.2f}
  Add-ons      : ${booking.addons_total_at_booking:.2f}
  Total        : ${booking.subtotal:.2f} inc. GST

SPECIAL INSTRUCTIONS
  {booking.special_instructions or 'None'}

──────────────────────────────
View in admin: http://127.0.0.1:8000/admin/bookings/booking/{booking.id}/change/
"""

    send_mail(
        subject=subject,
        message=body,
        from_email=_get_from_email(),
        recipient_list=[admin_email],
        fail_silently=False,
    )
