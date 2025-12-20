# Setup Script for UHV Project
# Run this in PowerShell

Write-Host "Setting up UHV Project..." -ForegroundColor Green

# 1. Install Dependencies
Write-Host "Installing dependencies..."
pip install -r requirements.txt

# 2. Apply Migrations
Write-Host "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# 3. Create Superuser (Optional - Interactive)
Write-Host "NOTE: You can create a superuser for Admin Panel using 'python manage.py createsuperuser'"

# 4. Load Initial Data (Population script logic could be here, but we will rely on user using Admin)
# However, let's create a script to seed some data for immediate demo satisfaction
python seed_data.py

# 5. Run Server
Write-Host "Setup complete. Run 'python manage.py runserver' to start."
