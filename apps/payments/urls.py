from django.urls import path
from . import views
from . import webhooks

app_name = 'payments'

urlpatterns = [
    path('checkout/<str:reference>/', views.checkout_view, name='checkout'),
    path('success/<str:reference>/', views.payment_success_view, name='payment_success'),
    path('webhooks/stripe/', webhooks.stripe_webhook, name='stripe_webhook'),
]
