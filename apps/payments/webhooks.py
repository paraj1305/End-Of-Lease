import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from apps.bookings.models import Booking
from apps.bookings.services.availability import is_date_available

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
        
    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        handle_payment_succeeded(intent)
        
    return HttpResponse(status=200)

def handle_payment_succeeded(intent):
    booking_id = intent['metadata'].get('booking_id')
    if not booking_id:
        return
        
    try:
        booking = Booking.objects.get(id=booking_id)
        
        if booking.status == 'draft':
            if not is_date_available(booking.booking_date):
                # Race condition: date is no longer available. Refund.
                stripe.Refund.create(payment_intent=intent['id'])
                booking.status = 'cancelled'
                booking.payment_status = 'refunded'
                booking.save()
            else:
                booking.status = 'confirmed'
                booking.payment_status = 'deposit_paid'
                booking.stripe_payment_intent_id = intent['id']
                booking.deposit_paid_at = timezone.now()
                booking.save()
    except Booking.DoesNotExist:
        pass
