import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .services.availability import get_availability_for_month, get_date_status
from .services.pricing import calculate_booking_price
from .models import CleaningPackage, AddOnService, TimeSlot, QuoteInquiry
from decimal import Decimal
from django.shortcuts import get_object_or_404
import datetime

@require_GET
def availability_api(request):
    """
    Returns availability for a specific month and year.
    /api/availability/?year=2024&month=11
    """
    try:
        year = int(request.GET.get('year'))
        month = int(request.GET.get('month'))
    except (TypeError, ValueError):
        now = datetime.datetime.now()
        year = now.year
        month = now.month

    availability = get_availability_for_month(year, month)
    return JsonResponse(availability)

@require_GET
def timeslots_api(request):
    """
    Returns available time slots for a given date.
    /api/timeslots/?date=YYYY-MM-DD
    """
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'Date parameter is required'}, status=400)
        
    try:
        target_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)
        
    status = get_date_status(target_date)
    if status != 'available':
        return JsonResponse({'slots': []})
        
    slots = TimeSlot.objects.filter(is_active=True).values('id', 'label', 'start_time')
    return JsonResponse({'slots': list(slots)})

@require_GET
def price_calculation_api(request):
    """
    Calculates the total price dynamically.
    /api/price/?package=1&addons=1,2,3
    """
    package_id = request.GET.get('package')
    addons_str = request.GET.get('addons', '')
    
    if not package_id:
        return JsonResponse({'error': 'Package ID is required'}, status=400)
        
    package = get_object_or_404(CleaningPackage, id=package_id, is_active=True)
    
    addon_ids = [int(x) for x in addons_str.split(',') if x.isdigit()]
    addons = AddOnService.objects.filter(id__in=addon_ids, is_active=True)
    
    addon_prices = [addon.price for addon in addons]
    
    pricing = calculate_booking_price(package.base_price, addon_prices)
    
    return JsonResponse({
        'subtotal': str(pricing['subtotal']),
        'addons_total': str(pricing['addons_total']),
        'deposit_amount': str(pricing['deposit_amount']),
        'remaining_amount': str(pricing['remaining_amount'])
    })


@csrf_exempt
@require_POST
def create_quote_inquiry_api(request):
    """
    Saves an inquiry submitted from the step form (Instant Quote Calculator).
    Accepts JSON payload or standard form POST.
    """
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST

        first_name = (data.get('firstName') or data.get('first_name') or '').strip()
        phone = (data.get('phone') or '').strip()
        email = (data.get('email') or '').strip()

        if not first_name or not phone:
            return JsonResponse({'success': False, 'error': 'Name and phone number are required.'}, status=400)

        preferred_date_raw = data.get('preferredDate') or data.get('preferred_date') or None
        preferred_date = None
        if preferred_date_raw:
            try:
                preferred_date = datetime.datetime.strptime(preferred_date_raw, '%Y-%m-%d').date()
            except ValueError:
                preferred_date = None

        preferred_time = (data.get('preferredTime') or data.get('preferred_time') or '').strip()
        try:
            bedrooms = int(data.get('bedrooms', 1))
        except (ValueError, TypeError):
            bedrooms = 1
        try:
            bathrooms = int(data.get('bathrooms', 1))
        except (ValueError, TypeError):
            bathrooms = 1
        try:
            living_areas = int(data.get('living_areas', 1))
        except (ValueError, TypeError):
            living_areas = 1
        try:
            balconies = int(data.get('balconies', 0))
        except (ValueError, TypeError):
            balconies = 0

        selected_addons = data.get('selectedAddons') or data.get('selected_addons') or {}
        if isinstance(selected_addons, str):
            try:
                selected_addons = json.loads(selected_addons)
            except Exception:
                selected_addons = {}

        additional_notes = (data.get('additionalNotes') or data.get('notes') or '').strip()
        try:
            estimated_price = Decimal(str(data.get('totalPrice') or data.get('estimated_price') or 0))
        except Exception:
            estimated_price = Decimal('0.00')

        inquiry = QuoteInquiry.objects.create(
            first_name=first_name[:150],
            phone=phone[:30],
            email=email,
            preferred_date=preferred_date,
            preferred_time=preferred_time[:50],
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            living_areas=living_areas,
            balconies=balconies,
            selected_addons=selected_addons,
            additional_notes=additional_notes,
            estimated_price=estimated_price,
            status='new',
        )

        return JsonResponse({
            'success': True,
            'inquiry_id': inquiry.id,
            'message': 'Inquiry successfully saved to database.'
        })
    except Exception as ex:
        return JsonResponse({'success': False, 'error': str(ex)}, status=500)

