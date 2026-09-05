from decimal import Decimal
from typing import List
from config import constants


def calculate_booking_price(package_price: Decimal, addon_prices: List[Decimal], deposit_percentage: Decimal = None) -> dict:
    """
    Calculates the subtotal, deposit, and remaining amount for a booking.
    """
    if deposit_percentage is None:
        deposit_percentage = Decimal(str(constants.DEPOSIT_PERCENTAGE))

    addons_total = sum(addon_prices)
    subtotal = package_price + addons_total
    
    deposit_amount = (subtotal * (deposit_percentage / Decimal('100.0'))).quantize(Decimal('0.01'))
    remaining_amount = subtotal - deposit_amount
    
    return {
        'subtotal': subtotal,
        'addons_total': addons_total,
        'deposit_amount': deposit_amount,
        'remaining_amount': remaining_amount
    }
