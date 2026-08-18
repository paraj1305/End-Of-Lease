from django import forms
from .models import Booking, BlockedDate
from django.utils import timezone
import datetime

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'customer_name', 'customer_email', 'customer_phone',
            'service_address_street', 'service_address_suburb',
            'service_address_state', 'service_address_postcode',
            'special_instructions'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe', 'required': True}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john@example.com', 'required': True}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0400 000 000', 'required': True}),
            'service_address_street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Fake Street', 'required': True}),
            'service_address_suburb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sydney', 'required': True}),
            'service_address_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NSW', 'required': True}),
            'service_address_postcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2000', 'required': True}),
            'special_instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional instructions (e.g. key under mat)'}),
        }
