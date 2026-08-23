from django.contrib import admin
from .models import CleaningPackage, AddOnService, TimeSlot, BlockedDate, Booking, BookingAddOn, PricingConfig

@admin.register(CleaningPackage)
class CleaningPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_price', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(AddOnService)
class AddOnServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('label', 'start_time', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    ordering = ('display_order', 'start_time')

@admin.register(BlockedDate)
class BlockedDateAdmin(admin.ModelAdmin):
    list_display = ('date', 'reason', 'blocked_by', 'created_at')
    list_filter = ('date',)
    search_fields = ('reason',)

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'base_fee', 'bedroom_price', 'bathroom_price', 'living_area_price', 'balcony_price')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

class BookingAddOnInline(admin.TabularInline):
    model = BookingAddOn
    extra = 0
    readonly_fields = ('price_at_booking',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('reference', 'customer_name', 'booking_date', 'time_slot', 'status', 'payment_status', 'subtotal')
    list_filter = ('status', 'payment_status', 'booking_date')
    search_fields = ('reference', 'customer_name', 'customer_email', 'customer_phone')
    readonly_fields = ('reference', 'created_at', 'updated_at', 'deposit_paid_at')
    inlines = [BookingAddOnInline]
    
    fieldsets = (
        ('Booking Details', {
            'fields': ('reference', 'status', 'payment_status', 'booking_date', 'time_slot')
        }),
        ('Customer Details', {
            'fields': ('customer_name', 'customer_email', 'customer_phone')
        }),
        ('Service Address', {
            'fields': ('service_address_street', 'service_address_suburb', 'service_address_state', 'service_address_postcode')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'living_areas', 'balconies')
        }),
        ('Pricing', {
            'fields': ('base_clean_price', 'addons_total_at_booking', 'subtotal', 'deposit_percentage', 'deposit_amount', 'remaining_amount', 'package', 'package_name_at_booking', 'package_price_at_booking')
        }),
        ('Additional Info', {
            'fields': ('special_instructions', 'admin_notes', 'stripe_payment_intent_id', 'google_calendar_event_id')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'deposit_paid_at')
        }),
    )
