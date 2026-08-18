from django.test import TestCase
from decimal import Decimal
import datetime
from apps.bookings.services.pricing import calculate_booking_price
from apps.bookings.services.availability import is_date_available
from apps.bookings.models import Booking, BlockedDate, TimeSlot, CleaningPackage

class PricingServiceTests(TestCase):
    def test_calculate_booking_price(self):
        package_price = Decimal('100.00')
        addons_prices = [Decimal('20.00'), Decimal('30.00')]
        
        result = calculate_booking_price(package_price, addons_prices)
        
        self.assertEqual(result['subtotal'], Decimal('150.00'))
        self.assertEqual(result['deposit_amount'], Decimal('15.00'))
        self.assertEqual(result['remaining_amount'], Decimal('135.00'))

class AvailabilityServiceTests(TestCase):
    def setUp(self):
        self.package = CleaningPackage.objects.create(name='Test', base_price=100)
        self.time_slot = TimeSlot.objects.create(label='Morning', start_time=datetime.time(8, 0))
        
    def test_is_date_available_no_blocks(self):
        date = datetime.date(2027, 1, 1)
        self.assertTrue(is_date_available(date))
        
    def test_is_date_available_with_blocked_date(self):
        date = datetime.date(2027, 1, 1)
        BlockedDate.objects.create(date=date, reason='Holiday')
        self.assertFalse(is_date_available(date))
        
    def test_is_date_available_with_confirmed_booking(self):
        date = datetime.date(2027, 1, 1)
        Booking.objects.create(
            package=self.package,
            booking_date=date,
            time_slot=self.time_slot,
            status='confirmed',
            package_name_at_booking='Test',
            package_price_at_booking=Decimal('100'),
            addons_total_at_booking=Decimal('0'),
            subtotal=Decimal('100'),
            deposit_amount=Decimal('10'),
            remaining_amount=Decimal('90')
        )
        # Assuming maximum capacity per slot is 1 by default, meaning if one is booked it might not be available,
        # but our logic checks if ANY slots are available.
        # Since we only created one time slot, and it's booked, the date should be unavailable.
        self.assertFalse(is_date_available(date))
