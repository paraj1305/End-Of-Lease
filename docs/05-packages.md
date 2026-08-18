# 05 — Cleaning Packages

## Overview
Cleaning packages are the primary product offering of the platform. They are fully admin-managed — no prices or package names are hardcoded in the application.

---

## Django Model

```python
# bookings/models.py

class CleaningPackage(models.Model):
    name = models.CharField(max_length=100)               # e.g., "2 BHK"
    slug = models.SlugField(unique=True)                  # e.g., "2-bhk"
    approximate_area = models.CharField(max_length=100)   # e.g., "600–800 sqft"
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    short_description = models.TextField()                # Used on landing page cards
    long_description = models.TextField(blank=True)       # Used on services detail page
    included_services = models.JSONField(default=list)    # List of strings
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name
```

---

## Default Packages (Placeholder — Client Must Confirm)

| Package | Approx. Area | Price (AUD) | Status |
|---------|-------------|-------------|--------|
| 2 BHK End of Lease | ~60–80 m² | TBD by client | Active |
| 3 BHK End of Lease | ~85–110 m² | TBD by client | Active |
| 4 BHK End of Lease | ~115–140 m² | TBD by client | Active |
| 5 BHK End of Lease | ~145–180 m² | TBD by client | Active |

> All prices, area ranges, and package names MUST be confirmed and set by the client via the admin panel before launch. Do not hardcode these values.

---

## Included Services (Example Placeholder)

For each package, the admin defines the list of included cleaning tasks. Example for a 3 BHK:
- All rooms vacuumed and mopped
- Kitchen: oven, stovetop, range hood, cupboards inside/out
- Bathrooms: tiles, grout, fixtures, mirrors
- Windows inside
- Skirting boards and light switches
- Walls (spot clean)
- Wardrobes inside/out

---

## Admin CRUD Requirements

| Action | Details |
|--------|---------|
| Create | Admin can add a new package via admin form |
| Read | Admin views list and detail of all packages |
| Update | Admin edits any field |
| Delete | Admin deletes a package (only if no bookings use it — or soft delete) |
| Activate | Sets `is_active = True` → visible to customers |
| Deactivate | Sets `is_active = False` → hidden from customers immediately |
| Reorder | Admin sets `display_order` to control landing page card sequence |

---

## Business Rules

1. Only packages where `is_active = True` are shown to customers.
2. Packages with existing bookings should NOT be permanently deleted; use deactivation.
3. Price changes apply to new bookings only; existing bookings retain their original price (stored at booking time).
4. The landing page package section and the booking flow both load packages dynamically from the database.
5. At least one active package must exist for the booking flow to work.

---

## Price Storage on Booking

When a booking is created, the following price fields are stored in the Booking model to preserve a point-in-time snapshot:
- `package_price_at_booking` — price of the package when the booking was made
- `addons_total_at_booking` — total of all selected add-ons
- `subtotal_at_booking` — package + add-ons
- `deposit_amount` — 10% of subtotal
- `remaining_amount` — 90% of subtotal

This ensures price changes don't retroactively affect existing bookings.

---

## Related Documents
- `06-addons.md`
- `07-booking-management.md`
- `09-payments.md`
