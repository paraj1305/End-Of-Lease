from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .services.availability import get_availability_for_month, get_date_status
from .services.pricing import calculate_booking_price
from .models import CleaningPackage, AddOnService, TimeSlot
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
