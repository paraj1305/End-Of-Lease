# 06 — Add-on Services

## Overview
Add-ons are optional additional cleaning services that customers can select during the booking flow. They are fully admin-managed — prices and names are not hardcoded.

---

## Django Model

```python
# bookings/models.py

class AddOnService(models.Model):
    name = models.CharField(max_length=100)       # e.g., "Garden Cleaning"
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # e.g., 20.00
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} (+${self.price})"
```

---

## Default Add-ons (Placeholder — Client Must Confirm)

| Add-on | Price (AUD) | Status |
|--------|-------------|--------|
| Garden Cleaning | TBD | Active |
| Garage Cleaning | TBD | Active |
| Bathroom Deep Cleaning | TBD | Active |
| *(Client-defined add-ons)* | TBD | TBD |

> All add-on names and prices MUST be confirmed and set by the client via the admin panel before launch.

---

## Admin CRUD Requirements

| Action | Details |
|--------|---------|
| Create | Admin adds a new add-on with name, description, price |
| Read | Admin views list of all add-ons |
| Update | Admin edits any field |
| Delete | Admin deletes an add-on (soft delete if referenced in bookings) |
| Activate | Sets `is_active = True` → visible to customers |
| Deactivate | Sets `is_active = False` → hidden from customers immediately |
| Reorder | Admin controls display order |

---

## Business Rules

1. Only add-ons where `is_active = True` are shown to customers.
2. Customers can select zero, one, or multiple add-ons.
3. Running total updates dynamically as the customer selects/deselects add-ons.
4. Add-on prices are summed and added to the package base price to calculate the subtotal.
5. The 10% deposit is calculated on the subtotal (package + all selected add-ons).
6. At booking creation, selected add-on prices are stored in the Booking record (point-in-time snapshot).
7. Add-ons with existing bookings should NOT be permanently deleted — use deactivation.

---

## Booking–Add-on Relationship

```python
# bookings/models.py

class BookingAddOn(models.Model):
    """Stores the add-on and its price at time of booking (snapshot)."""
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='booking_addons')
    addon = models.ForeignKey(AddOnService, on_delete=models.PROTECT)
    price_at_booking = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.addon.name} @ ${self.price_at_booking}"
```

---

## UX / Frontend Behaviour

- Add-ons are displayed as toggleable cards or checkboxes.
- Each card shows: name, short description, price (formatted as "+$XX").
- Selecting an add-on adds its price to the running total immediately (client-side calculation confirmed server-side).
- The running total is displayed prominently during add-on selection.
- On mobile, add-on cards should be large enough to tap easily (minimum 44px touch target).

---

## Related Documents
- `05-packages.md`
- `03-user-booking-flow.md`
- `09-payments.md`
