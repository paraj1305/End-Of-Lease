"""
payments/views.py

Stripe checkout is currently COMMENTED OUT (not live).
The checkout_view redirects directly to the success page.
Re-enable Stripe by un-commenting the blocks below and setting live keys in .env.
"""

from django.shortcuts import render, redirect, get_object_or_404
# from django.conf import settings
from apps.bookings.models import Booking
# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout_view(request, reference):
    """
    Stripe checkout — DISABLED until live keys are configured.
    Redirects straight to payment_success for now.
    """
    booking = get_object_or_404(Booking, reference=reference)

    # ── Stripe PaymentIntent (COMMENTED OUT) ──
    # if booking.status != 'draft':
    #     return redirect('payments:payment_success', reference=booking.reference)
    #
    # try:
    #     intent = stripe.PaymentIntent.create(
    #         amount=int(booking.deposit_amount * 100),
    #         currency='aud',
    #         metadata={
    #             'booking_id': str(booking.id),
    #             'booking_reference': booking.reference,
    #         }
    #     )
    #     context = {
    #         'booking': booking,
    #         'client_secret': intent.client_secret,
    #         'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    #     }
    #     return render(request, 'payments/checkout.html', context)
    # except Exception as e:
    #     return render(request, 'payments/error.html', {'error': str(e)})

    return redirect('payments:payment_success', reference=booking.reference)


def payment_success_view(request, reference):
    booking = get_object_or_404(Booking, reference=reference)
    booking_addons = booking.booking_addons.select_related('addon').all()
    return render(request, 'payments/success.html', {
        'booking': booking,
        'booking_addons': booking_addons,
    })
