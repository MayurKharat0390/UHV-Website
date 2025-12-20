import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("🎛️  UHV Admin Setup")
print("=" * 50)
print()

# Check if superuser already exists
if User.objects.filter(is_superuser=True).exists():
    print("⚠️  A superuser already exists!")
    existing = User.objects.filter(is_superuser=True).first()
    print(f"   Username: {existing.username}")
    print()
    response = input("Create another superuser? (y/n): ")
    if response.lower() != 'y':
        print("Exiting...")
        exit()

print("Create your admin account:")
print()

username = input("Username: ")
email = input("Email (optional, press Enter to skip): ")
password = input("Password: ")
password2 = input("Password (again): ")

if password != password2:
    print("❌ Passwords don't match!")
    exit()

try:
    user = User.objects.create_superuser(
        username=username,
        email=email if email else '',
        password=password
    )
    print()
    print("✅ Superuser created successfully!")
    print()
    print(f"📍 Access admin panel at: http://127.0.0.1:8000/admin/")
    print(f"   Username: {username}")
    print()
    print("📖 Read ADMIN_GUIDE.md for complete documentation")
except Exception as e:
    print(f"❌ Error: {e}")
