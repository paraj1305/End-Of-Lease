from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from apps.bookings.models import Booking
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_view(request, reference):
    booking = get_object_or_404(Booking, reference=reference)
    
    if booking.status != 'draft':
        return redirect('payments:payment_success', reference=booking.reference)
        
    try:
        # Create a PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=int(booking.deposit_amount * 100),  # Convert to cents
            currency='aud',
            metadata={
                'booking_id': str(booking.id),
                'booking_reference': booking.reference,
            }
        )
        
        context = {
            'booking': booking,
            'client_secret': intent.client_secret,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        }
        return render(request, 'payments/checkout.html', context)
        
    except Exception as e:
        return render(request, 'payments/error.html', {'error': str(e)})

def payment_success_view(request, reference):
    booking = get_object_or_404(Booking, reference=reference)
    return render(request, 'payments/success.html', {'booking': booking})
