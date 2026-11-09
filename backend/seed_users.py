import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voltora_backend.settings')
django.setup()

from apps.users.models import User

def seed():
    # 1. Admin
    admin_user, created = User.objects.get_or_create(
        email='admin@voltora.com',
        defaults={
            'username': 'admin',
            'first_name': 'Voltora',
            'last_name': 'Admin',
            'role': 'admin',
            'is_staff': True,
            'is_superuser': True,
            'city': 'Hyderabad',
            'kyc_status': 'verified',
            'is_verified_seller': True,
        }
    )
    admin_user.set_password('admin123')
    admin_user.save()
    print("Admin user ready: admin@voltora.com / admin123")

    # 2. Seller
    seller_user, created = User.objects.get_or_create(
        email='seller@voltora.com',
        defaults={
            'username': 'hyd_ev_rentals',
            'first_name': 'Rajesh',
            'last_name': 'Kumar',
            'role': 'seller',
            'phone': '+91 98765 43210',
            'city': 'Hyderabad',
            'address': 'Plot 42, Silicon Valley, Madhapur, Hyderabad, TS 500081',
            'kyc_status': 'verified',
            'is_verified_seller': True,
            'driving_licence_number': 'TS09-20210048291',
            'id_card_type': 'Aadhaar Card',
            'id_card_number': '8472-9182-3918',
        }
    )
    seller_user.set_password('seller123')
    seller_user.save()
    print("Seller user ready: seller@voltora.com / seller123")

    # 3. Customer
    cust_user, created = User.objects.get_or_create(
        email='customer@voltora.com',
        defaults={
            'username': 'ananya_sharma',
            'first_name': 'Ananya',
            'last_name': 'Sharma',
            'role': 'customer',
            'phone': '+91 91234 56789',
            'city': 'Hyderabad',
            'address': 'Flat 304, Green Meadows, Gachibowli, Hyderabad, TS 500032',
            'kyc_status': 'verified',
            'driving_licence_number': 'TS09-20220019284',
            'id_card_type': 'Aadhaar Card',
            'id_card_number': '5192-3847-1928',
        }
    )
    cust_user.set_password('customer123')
    cust_user.save()
    print("Customer user ready: customer@voltora.com / customer123")

if __name__ == '__main__':
    seed()
