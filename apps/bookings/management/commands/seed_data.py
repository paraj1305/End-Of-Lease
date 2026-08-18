import datetime
from django.core.management.base import BaseCommand
from apps.bookings.models import CleaningPackage, AddOnService, TimeSlot

class Command(BaseCommand):
    help = 'Seed initial placeholder data for MVP'

    def handle(self, *args, **kwargs):
        # 1. Cleaning Packages
        packages = [
            {
                'name': '[PLACEHOLDER] 1 BHK Cleaning',
                'slug': '1-bhk-cleaning',
                'approximate_area': '~ 40 - 60 sqm',
                'base_price': 199.00,
                'short_description': 'Perfect for a 1 bedroom, 1 bathroom apartment.',
                'display_order': 1,
            },
            {
                'name': '[PLACEHOLDER] 2 BHK Cleaning',
                'slug': '2-bhk-cleaning',
                'approximate_area': '~ 60 - 90 sqm',
                'base_price': 299.00,
                'short_description': 'Ideal for a 2 bedroom apartment or small house.',
                'display_order': 2,
            },
            {
                'name': '[PLACEHOLDER] 3 BHK Cleaning',
                'slug': '3-bhk-cleaning',
                'approximate_area': '~ 90 - 150 sqm',
                'base_price': 399.00,
                'short_description': 'For a 3 bedroom house with up to 2 bathrooms.',
                'display_order': 3,
            },
        ]
        
        for pkg_data in packages:
            CleaningPackage.objects.get_or_create(
                slug=pkg_data['slug'],
                defaults=pkg_data
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded packages'))

        # 2. Add-on Services
        addons = [
            {
                'name': '[PLACEHOLDER] Balcony Cleaning',
                'slug': 'balcony-cleaning',
                'short_description': 'High-pressure wash and scrub of outdoor balcony.',
                'price': 40.00,
                'display_order': 1,
            },
            {
                'name': '[PLACEHOLDER] Garage Sweeping',
                'slug': 'garage-sweeping',
                'short_description': 'Thorough sweep and cobweb removal in the garage.',
                'price': 30.00,
                'display_order': 2,
            },
            {
                'name': '[PLACEHOLDER] Blinds Cleaning',
                'slug': 'blinds-cleaning',
                'short_description': 'Detailed dusting and wiping of all blinds.',
                'price': 60.00,
                'display_order': 3,
            }
        ]

        for addon_data in addons:
            AddOnService.objects.get_or_create(
                slug=addon_data['slug'],
                defaults=addon_data
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded add-ons'))

        # 3. Time Slots
        time_slots = [
            {'label': 'Morning (8:00 AM)', 'start_time': datetime.time(8, 0), 'display_order': 1},
            {'label': 'Mid-day (11:00 AM)', 'start_time': datetime.time(11, 0), 'display_order': 2},
            {'label': 'Afternoon (2:00 PM)', 'start_time': datetime.time(14, 0), 'display_order': 3},
        ]

        for slot_data in time_slots:
            TimeSlot.objects.get_or_create(
                start_time=slot_data['start_time'],
                defaults=slot_data
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded time slots'))
