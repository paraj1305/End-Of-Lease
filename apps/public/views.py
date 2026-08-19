from django.shortcuts import render
from apps.bookings.models import CleaningPackage, AddOnService
from .models import FAQ

def home_view(request):
    packages = CleaningPackage.objects.filter(is_active=True)[:4]
    addons = AddOnService.objects.filter(is_active=True)[:6]
    faqs = FAQ.objects.filter(is_active=True).order_by('order')
    return render(request, 'public/home.html', {
        'packages': packages, 
        'addons': addons,
        'faqs': faqs
    })

def about_view(request):
    return render(request, 'public/about.html')

def services_view(request):
    packages = CleaningPackage.objects.filter(is_active=True)
    return render(request, 'public/services.html', {'packages': packages})

def contact_view(request):
    return render(request, 'public/contact.html')

def faq_view(request):
    faqs = FAQ.objects.filter(is_active=True).order_by('order')
    return render(request, 'public/faq.html', {'faqs': faqs})

def our_work_view(request):
    return render(request, 'public/our_work.html')
