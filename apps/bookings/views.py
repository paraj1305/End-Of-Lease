from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import CleaningPackage, AddOnService, TimeSlot, Booking, BookingAddOn, PricingConfig
from .forms import CustomerDetailsForm
from .services.pricing import calculate_booking_price
from .emails import send_booking_confirmation
import datetime


def quick_book(request, package_slug):
    """Redirects to main booking page (/book/) with pre-filled property counters from selected package."""
    import re
    package = CleaningPackage.objects.filter(slug=package_slug, is_active=True).first()
    
    if package:
        bedrooms = package.bedrooms
        bathrooms = package.bathrooms
        living = package.living_areas
        balconies = package.balconies
    else:
        # Fallback for dynamic / regex matching
        bhk_match = re.search(r'(\d+)[-_]?(?:bhk|bed)', package_slug.lower())
        if bhk_match:
            beds = int(bhk_match.group(1))
            bedrooms = beds
            bathrooms = max(1, beds // 2 + (1 if beds > 1 else 0))
            living = 1 if beds <= 3 else 2
            balconies = 1 if beds >= 2 else 0
        else:
            bedrooms, bathrooms, living, balconies = 1, 1, 1, 0

    query_str = f"?bedrooms={bedrooms}&bathrooms={bathrooms}&living={living}&balconies={balconies}&package={package_slug}"
    return redirect(reverse('bookings:multi_step_booking') + query_str)


def multi_step_booking(request):
    """Single-page Alpine.js booking form with dynamic property pricing."""
    pricing_config = PricingConfig.get_solo()
    addons = AddOnService.objects.filter(is_active=True)
    time_slots = TimeSlot.objects.filter(is_active=True)

    if request.method == 'POST':
        try:
            bedrooms = int(request.POST.get('bedrooms', 1))
            bathrooms = int(request.POST.get('bathrooms', 1))
            living_areas = int(request.POST.get('living_areas', 1))
            balconies = int(request.POST.get('balconies', 0))
        except ValueError:
            bedrooms, bathrooms, living_areas, balconies = 1, 1, 1, 0

        name = request.POST.get('customer_name', '').strip()
        email = request.POST.get('customer_email', '').strip()
        phone = request.POST.get('customer_phone', '').strip()
        street = request.POST.get('service_address_street', '').strip()
        suburb = request.POST.get('service_address_suburb', '').strip()
        postcode = request.POST.get('service_address_postcode', '').strip()
        state = request.POST.get('service_address_state', 'NSW').strip()
        addr_query = request.POST.get('addr_query', '').strip()

        # Fallback if user manually typed address without clicking dropdown
        if not street and addr_query:
            parts = [p.strip() for p in addr_query.split(',') if p.strip()]
            street = parts[0] if parts else addr_query
            if not suburb and len(parts) > 1:
                suburb = parts[1]
            if not suburb:
                suburb = 'Sydney'
            if not postcode:
                import re
                pc_match = re.search(r'\b\d{4}\b', addr_query)
                postcode = pc_match.group(0) if pc_match else '2000'

        date_str = request.POST.get('booking_date', '').strip()
        time_slot_id = request.POST.get('time_slot_id', '').strip()
        addon_ids = request.POST.getlist('addon_ids')
        special_instructions = request.POST.get('special_instructions', '').strip()

        errors = []

        if not all([name, email, phone, street, suburb, postcode, date_str, time_slot_id]):
            errors.append('Please fill in all required fields.')

        booking_date = None
        try:
            booking_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if booking_date < datetime.date.today():
                errors.append('Please select a future date.')
        except (ValueError, TypeError):
            errors.append('Invalid date format.')

        time_slot = None
        try:
            time_slot = TimeSlot.objects.get(id=int(time_slot_id), is_active=True)
        except (TimeSlot.DoesNotExist, ValueError):
            errors.append('Please select a valid time slot.')

        selected_addons = AddOnService.objects.filter(id__in=[int(a) for a in addon_ids if a.isdigit()])

        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            from decimal import Decimal
            beds = max(1, int(bedrooms))
            baths = max(1, int(bathrooms))
            raw_price = 259 + 82 * (beds - 1) + 34 * (baths - 1)
            if beds == 1 and baths == 1:
                base_clean_price = Decimal("259.00")
            else:
                base_clean_price = Decimal(str(round(raw_price / 5) * 5))

            pricing = calculate_booking_price(base_clean_price, [a.price for a in selected_addons])

            booking = Booking.objects.create(
                package=None, # No package
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                living_areas=living_areas,
                balconies=balconies,
                base_clean_price=base_clean_price,
                addons_total_at_booking=pricing['addons_total'],
                subtotal=pricing['subtotal'],
                deposit_amount=pricing['deposit_amount'],
                remaining_amount=pricing['remaining_amount'],
                booking_date=booking_date,
                time_slot=time_slot,
                customer_name=name,
                customer_email=email,
                customer_phone=phone,
                service_address_street=street,
                service_address_suburb=suburb,
                service_address_postcode=postcode,
                service_address_state=state,
                special_instructions=special_instructions,
            )

            for addon in selected_addons:
                BookingAddOn.objects.create(
                    booking=booking,
                    addon=addon,
                    price_at_booking=addon.price,
                )

            # ── Confirm booking ──
            booking.status = 'confirmed'
            booking.save()

            # ── Send emails (customer + admin) ──
            try:
                send_booking_confirmation(booking)
            except Exception:
                # Email failure should not break the booking flow
                pass

            # ── Payment gateway (Stripe) — COMMENTED OUT, not live yet ──
            # return redirect('payments:checkout', reference=booking.reference)

            return redirect('payments:payment_success', reference=booking.reference)

    context = {
        'pricing_config': pricing_config,
        'addons': addons,
        'time_slots': time_slots,
        'min_date': datetime.date.today().strftime('%Y-%m-%d'),
    }
    return render(request, 'bookings/book.html', context)

def get_booking_session(request):
    if 'booking_data' not in request.session:
        request.session['booking_data'] = {
            'package_id': None,
            'addon_ids': [],
            'date': None,
            'time_slot_id': None,
            'customer_details': {}
        }
    return request.session['booking_data']

def save_booking_session(request, data):
    request.session['booking_data'] = data
    request.session.modified = True

def clear_booking_session(request):
    if 'booking_data' in request.session:
        del request.session['booking_data']

def step_1_package(request):
    packages = CleaningPackage.objects.filter(is_active=True)
    session_data = get_booking_session(request)
    
    if request.method == 'POST':
        package_id = request.POST.get('package_id')
        if package_id and CleaningPackage.objects.filter(id=package_id, is_active=True).exists():
            session_data['package_id'] = int(package_id)
            save_booking_session(request, session_data)
            return redirect('bookings:step_2_addons')
        else:
            messages.error(request, 'Please select a valid package.')
            
    context = {
        'packages': packages,
        'selected_package': session_data.get('package_id')
    }
    return render(request, 'bookings/steps/step_1_package.html', context)

def step_2_addons(request):
    session_data = get_booking_session(request)
    if not session_data.get('package_id'):
        return redirect('bookings:step_1_package')
        
    addons = AddOnService.objects.filter(is_active=True)
    
    if request.method == 'POST':
        addon_ids = request.POST.getlist('addon_ids')
        session_data['addon_ids'] = [int(aid) for aid in addon_ids if aid.isdigit()]
        save_booking_session(request, session_data)
        return redirect('bookings:step_3_datetime')
        
    context = {
        'addons': addons,
        'selected_addons': session_data.get('addon_ids', [])
    }
    return render(request, 'bookings/steps/step_2_addons.html', context)

def step_3_datetime(request):
    session_data = get_booking_session(request)
    if not session_data.get('package_id'):
        return redirect('bookings:step_1_package')
        
    if request.method == 'POST':
        date_str = request.POST.get('date')
        time_slot_id = request.POST.get('time_slot_id')
        
        if date_str and time_slot_id:
            try:
                datetime.datetime.strptime(date_str, '%Y-%m-%d')
                if TimeSlot.objects.filter(id=time_slot_id, is_active=True).exists():
                    session_data['date'] = date_str
                    session_data['time_slot_id'] = int(time_slot_id)
                    save_booking_session(request, session_data)
                    return redirect('bookings:step_4_details')
            except ValueError:
                pass
        
        messages.error(request, 'Please select a valid date and time slot.')

    # Get active time slots for the initial load if we don't have JS
    time_slots = TimeSlot.objects.filter(is_active=True)

    context = {
        'time_slots': time_slots,
        'selected_date': session_data.get('date'),
        'selected_time_slot': session_data.get('time_slot_id')
    }
    return render(request, 'bookings/steps/step_3_datetime.html', context)

def step_4_details(request):
    session_data = get_booking_session(request)
    if not session_data.get('date') or not session_data.get('time_slot_id'):
        return redirect('bookings:step_3_datetime')
        
    initial_data = session_data.get('customer_details', {})
    
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            session_data['customer_details'] = form.cleaned_data
            save_booking_session(request, session_data)
            return redirect('bookings:step_5_review')
    else:
        form = CustomerDetailsForm(initial=initial_data)
        
    context = {
        'form': form
    }
    return render(request, 'bookings/steps/step_4_details.html', context)

def step_5_review(request):
    session_data = get_booking_session(request)
    if not session_data.get('customer_details'):
        return redirect('bookings:step_4_details')
        
    package = get_object_or_404(CleaningPackage, id=session_data['package_id'])
    addons = AddOnService.objects.filter(id__in=session_data.get('addon_ids', []))
    time_slot = get_object_or_404(TimeSlot, id=session_data['time_slot_id'])
    
    pricing = calculate_booking_price(package.base_price, [a.price for a in addons])
    
    context = {
        'package': package,
        'addons': addons,
        'date': session_data['date'],
        'time_slot': time_slot,
        'customer_details': session_data['customer_details'],
        'pricing': pricing
    }
    
    if request.method == 'POST':
        # Create the booking object (status: draft)
        booking = Booking.objects.create(
            package=package,
            package_name_at_booking=package.name,
            package_price_at_booking=package.base_price,
            addons_total_at_booking=pricing['addons_total'],
            subtotal=pricing['subtotal'],
            deposit_amount=pricing['deposit_amount'],
            remaining_amount=pricing['remaining_amount'],
            booking_date=session_data['date'],
            time_slot=time_slot,
            **session_data['customer_details']
        )
        
        for addon in addons:
            BookingAddOn.objects.create(
                booking=booking,
                addon=addon,
                price_at_booking=addon.price
            )
            
        # ── Confirm booking ──
        booking.status = 'confirmed'
        booking.save()

        # ── Send emails (customer + admin) ──
        try:
            send_booking_confirmation(booking)
        except Exception:
            pass

        clear_booking_session(request)

        # ── Payment gateway (Stripe) — COMMENTED OUT, not live yet ──
        # Store the created booking ID in session for payment flow
        # request.session['draft_booking_id'] = booking.id
        # return redirect('payments:checkout', reference=booking.reference)

        return redirect('payments:payment_success', reference=booking.reference)
        
    return render(request, 'bookings/steps/step_5_review.html', context)
