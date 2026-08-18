import datetime
from django.utils import timezone
from apps.bookings.models import Booking, BlockedDate, TimeSlot

def get_date_status(target_date: datetime.date) -> str:
    """
    Returns the status of a specific date: 'available', 'booked', or 'blocked'.
    """
    if target_date < timezone.localdate():
        return 'blocked' # Past dates are implicitly blocked
        
    if BlockedDate.objects.filter(date=target_date).exists():
        return 'blocked'
        
    if Booking.objects.filter(booking_date=target_date, status__in=['confirmed', 'completed']).exists():
        return 'booked'
        
    return 'available'

def is_date_available(target_date: datetime.date) -> bool:
    """
    Returns True if the date can be booked, False otherwise.
    """
    return get_date_status(target_date) == 'available'

def get_availability_for_month(year: int, month: int) -> dict:
    """
    Returns a dictionary mapping date string (YYYY-MM-DD) to status ('available', 'booked', 'blocked')
    for a given month.
    """
    import calendar
    _, num_days = calendar.monthrange(year, month)
    
    start_date = datetime.date(year, month, 1)
    end_date = datetime.date(year, month, num_days)
    
    # Batch query the blocked and booked dates
    blocked_dates = set(BlockedDate.objects.filter(
        date__range=[start_date, end_date]
    ).values_list('date', flat=True))
    
    booked_dates = set(Booking.objects.filter(
        booking_date__range=[start_date, end_date],
        status__in=['confirmed', 'completed']
    ).values_list('booking_date', flat=True))
    
    today = timezone.localdate()
    
    availability = {}
    for day in range(1, num_days + 1):
        current_date = datetime.date(year, month, day)
        date_str = current_date.isoformat()
        
        if current_date < today:
            availability[date_str] = 'blocked'
        elif current_date in blocked_dates:
            availability[date_str] = 'blocked'
        elif current_date in booked_dates:
            availability[date_str] = 'booked'
        else:
            availability[date_str] = 'available'
            
    return availability
