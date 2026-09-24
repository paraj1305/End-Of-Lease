import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CleaningPackage(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    approximate_area = models.CharField(max_length=100, blank=True)
    
    # Property room counts for dynamic pricing
    bedrooms = models.IntegerField(default=1, help_text="Number of bedrooms")
    bathrooms = models.IntegerField(default=1, help_text="Number of bathrooms")
    living_areas = models.IntegerField(default=1, help_text="Number of living areas")
    balconies = models.IntegerField(default=0, help_text="Number of balconies")

    base_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="Auto-synced or fallback base price")
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    included_services = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']

    @property
    def calculated_price(self):
        """Calculate package price dynamically based on formula: 259 + 82(Bed-1) + 34(Bath-1)."""
        from decimal import Decimal
        beds = max(1, self.bedrooms)
        baths = max(1, self.bathrooms)
        raw = 259 + 82 * (beds - 1) + 34 * (baths - 1)
        if beds == 1 and baths == 1:
            return Decimal("259.00")
        return Decimal(str(round(raw / 5) * 5))

    def save(self, *args, **kwargs):
        # Auto-update base_price if not manually locked
        try:
            self.base_price = self.calculated_price
        except Exception:
            pass
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.bedrooms}B/{self.bathrooms}B - ${self.calculated_price})"


class PricingConfig(models.Model):
    """Singleton model to store base pricing for properties."""
    base_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, help_text="Fixed base fee for all bookings.")
    bedroom_price = models.DecimalField(max_digits=8, decimal_places=2, default=49.00)
    bathroom_price = models.DecimalField(max_digits=8, decimal_places=2, default=30.00)
    living_area_price = models.DecimalField(max_digits=8, decimal_places=2, default=15.00)
    balcony_price = models.DecimalField(max_digits=8, decimal_places=2, default=10.00)
    
    class Meta:
        verbose_name = "Pricing Configuration"
        verbose_name_plural = "Pricing Configuration"

    def __str__(self):
        return "Current Pricing Configuration"

    @classmethod
    def get_solo(cls):
        from django.core.cache import cache
        obj = cache.get('pricing_config_solo')
        if obj is None:
            obj, _ = cls.objects.get_or_create(id=1)
            cache.set('pricing_config_solo', obj, 3600)
        return obj

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from django.core.cache import cache
        cache.set('pricing_config_solo', self, 3600)


class AddOnService(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.TextField()
    image = models.ImageField(upload_to='addons/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} (+${self.price})"


class TimeSlot(models.Model):
    label = models.CharField(max_length=50)
    start_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'start_time']

    def __str__(self):
        return self.label


class BlockedDate(models.Model):
    date = models.DateField(unique=True)
    reason = models.CharField(max_length=255, blank=True)
    blocked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return f"Blocked: {self.date}"


class Booking(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('deposit_paid', 'Deposit Paid'),
        ('fully_paid', 'Fully Paid'),
        ('refunded', 'Refunded'),
    )

    reference = models.CharField(max_length=20, unique=True, blank=True)
    package = models.ForeignKey(CleaningPackage, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Property Details (New Architecture)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    living_areas = models.IntegerField(default=1)
    balconies = models.IntegerField(default=0)
    base_clean_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    # Legacy fields
    package_name_at_booking = models.CharField(max_length=100, blank=True)
    package_price_at_booking = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    addons_total_at_booking = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    deposit_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    deposit_amount = models.DecimalField(max_digits=8, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=8, decimal_places=2)
    
    booking_date = models.DateField()
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT)
    
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=254)
    customer_phone = models.CharField(max_length=20)
    service_address_street = models.CharField(max_length=255)
    service_address_suburb = models.CharField(max_length=100)
    service_address_postcode = models.CharField(max_length=10)
    service_address_state = models.CharField(max_length=50)
    special_instructions = models.TextField(blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True)
    stripe_session_id = models.CharField(max_length=255, blank=True)
    deposit_paid_at = models.DateTimeField(null=True, blank=True)
    admin_notes = models.TextField(blank=True)
    
    # Phase 2 — blank in MVP
    google_calendar_event_id = models.CharField(max_length=255, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['booking_date', 'status']),
            models.Index(fields=['customer_email']),
            models.Index(fields=['reference']),
        ]

    def save(self, *args, **kwargs):
        if not self.reference:
            # Generate a unique reference e.g., EOL-XXXXX
            import random
            import string
            while True:
                ref = 'EOL-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                if not Booking.objects.filter(reference=ref).exists():
                    self.reference = ref
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference} - {self.customer_name} on {self.booking_date}"


class BookingAddOn(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='booking_addons')
    addon = models.ForeignKey(AddOnService, on_delete=models.PROTECT)
    price_at_booking = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.addon.name} for {self.booking.reference}"
