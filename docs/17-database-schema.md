# 17 — Database Schema

## Overview
Complete database schema for all models in the MVP.

---

## Entity Relationship Diagram

```
CleaningPackage ──< Booking >── BookingAddOn >── AddOnService
                        │
                        ├── TimeSlot
                        └── (date)
                        
BlockedDate (standalone — used for availability checks)
TimeSlot (standalone — admin-configured slots)
```

---

## Tables

### cleaning_package
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PK, AUTO |
| name | VARCHAR(100) | NOT NULL |
| slug | VARCHAR(100) | UNIQUE, NOT NULL |
| approximate_area | VARCHAR(100) | NOT NULL |
| base_price | DECIMAL(8,2) | NOT NULL |
| short_description | TEXT | NOT NULL |
| long_description | TEXT | |
| included_services | JSON | DEFAULT [] |
| is_active | BOOLEAN | DEFAULT TRUE |
| display_order | INTEGER | DEFAULT 0 |
| created_at | TIMESTAMP | AUTO |
| updated_at | TIMESTAMP | AUTO |

### addon_service
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PK, AUTO |
| name | VARCHAR(100) | NOT NULL |
| slug | VARCHAR(100) | UNIQUE |
| short_description | TEXT | NOT NULL |
| price | DECIMAL(8,2) | NOT NULL |
| is_active | BOOLEAN | DEFAULT TRUE |
| display_order | INTEGER | DEFAULT 0 |
| created_at | TIMESTAMP | AUTO |
| updated_at | TIMESTAMP | AUTO |

### time_slot
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PK, AUTO |
| label | VARCHAR(50) | NOT NULL |
| start_time | TIME | NOT NULL |
| is_active | BOOLEAN | DEFAULT TRUE |
| display_order | INTEGER | DEFAULT 0 |

### booking
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PK, AUTO |
| reference | VARCHAR(20) | UNIQUE, NOT NULL |
| package_id | INTEGER | FK → cleaning_package |
| package_name_at_booking | VARCHAR(100) | NOT NULL |
| package_price_at_booking | DECIMAL(8,2) | NOT NULL |
| addons_total_at_booking | DECIMAL(8,2) | DEFAULT 0 |
| subtotal | DECIMAL(8,2) | NOT NULL |
| deposit_percentage | DECIMAL(5,2) | DEFAULT 10 |
| deposit_amount | DECIMAL(8,2) | NOT NULL |
| remaining_amount | DECIMAL(8,2) | NOT NULL |
| booking_date | DATE | NOT NULL |
| time_slot_id | INTEGER | FK → time_slot |
| customer_name | VARCHAR(200) | NOT NULL |
| customer_email | VARCHAR(254) | NOT NULL |
| customer_phone | VARCHAR(20) | NOT NULL |
| service_address_street | VARCHAR(255) | NOT NULL |
| service_address_suburb | VARCHAR(100) | NOT NULL |
| service_address_postcode | VARCHAR(10) | NOT NULL |
| service_address_state | VARCHAR(50) | NOT NULL |
| special_instructions | TEXT | |
| status | VARCHAR(20) | DEFAULT 'draft' |
| payment_status | VARCHAR(50) | DEFAULT 'pending' |
| stripe_payment_intent_id | VARCHAR(255) | |
| stripe_session_id | VARCHAR(255) | |
| deposit_paid_at | TIMESTAMP | NULLABLE |
| admin_notes | TEXT | |
| google_calendar_event_id | VARCHAR(255) | (Phase 2 — blank in MVP) |
| created_at | TIMESTAMP | AUTO |
| updated_at | TIMESTAMP | AUTO |

> **Index:** `booking_date` + `status` (for fast availability checks)

### booking_addon
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PK, AUTO |
| booking_id | INTEGER | FK → booking |
| addon_id | INTEGER | FK → addon_service |
| price_at_booking | DECIMAL(8,2) | NOT NULL |

### blocked_date
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PK, AUTO |
| date | DATE | UNIQUE, NOT NULL |
| reason | VARCHAR(255) | |
| blocked_by_id | INTEGER | FK → auth_user (NULLABLE) |
| created_at | TIMESTAMP | AUTO |

---

## Key Indexes

```sql
-- Fast availability lookup
CREATE INDEX idx_booking_date_status ON booking (booking_date, status);

-- Admin search by customer
CREATE INDEX idx_booking_email ON booking (customer_email);
CREATE INDEX idx_booking_reference ON booking (reference);

-- Blocked date lookup
CREATE INDEX idx_blocked_date ON blocked_date (date);
```

---

## Related Documents
- `07-booking-management.md`
- `05-packages.md`
- `06-addons.md`
- `08-availability-and-calendar.md`
