from django.urls import path
from . import api
from . import views

app_name = 'bookings'

urlpatterns = [
    # API endpoints
    path('api/availability/', api.availability_api, name='api_availability'),
    path('api/timeslots/', api.timeslots_api, name='api_timeslots'),
    path('api/price/', api.price_calculation_api, name='api_price'),

    # Quick single-page booking (new)
    path('book/<slug:package_slug>/', views.quick_book, name='quick_book'),

    # Legacy multi-step wizard
    path('book/package/', views.step_1_package, name='step_1_package'),
    path('book/addons/', views.step_2_addons, name='step_2_addons'),
    path('book/datetime/', views.step_3_datetime, name='step_3_datetime'),
    path('book/details/', views.step_4_details, name='step_4_details'),
    path('book/review/', views.step_5_review, name='step_5_review'),
]
