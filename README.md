<<<<<<< HEAD
# End of Lease Cleaning Booking System

A Django web application for booking end-of-lease cleaning services.

## Prerequisites
- Python 3.x
- Git (optional, for version control)

## Setup & Installation

1. **Open a terminal (Command Prompt or PowerShell)** and navigate to the project folder:
   ```cmd
   cd "d:\pajju's projects\End of lease"
   ```

2. **Activate the virtual environment:**
   ```cmd
   .venv\Scripts\activate
   ```

3. **Install dependencies** (if not already installed):
   ```cmd
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```cmd
   python manage.py migrate
   ```

5. **(Optional) Create a superuser account** to access the Django admin panel (`/admin`):
   ```cmd
   python manage.py createsuperuser
   ```

## Running the Application

To start the development server, run:
```cmd
python manage.py runserver
```

Once the server is running, you can access the application in your web browser at:
- **Main Website:** `http://127.0.0.1:8000/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`

## Key Features
- **Public Pages:** Home, About, Services, Pricing, FAQ, Contact
- **Booking Flow:** Fully integrated, liquid-glass designed booking form with dynamic price calculation and add-on selection.
- **Payments:** Stripe integration for collecting a 10% upfront deposit securely.
- **Admin Management:** Manage packages, add-ons (with image support), bookings, and time slots via the Django Admin interface.
=======
# End-Of-Lease
>>>>>>> df794b65babec01d16fbac129b4f8c197a14e40c
