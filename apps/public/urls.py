from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('our-work/', views.our_work_view, name='our_work'),
    path('terms/', views.terms_view, name='terms'),
    path('guarantee-rules/', views.guarantee_rules_view, name='guarantee_rules'),
    path('checklist/pdf/', views.checklist_pdf_view, name='checklist_pdf'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
]
