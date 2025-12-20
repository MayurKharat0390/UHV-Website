# Create Superuser Script
Write-Host "🎛️  UHV Admin Setup" -ForegroundColor Cyan
Write-Host "==================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Creating superuser account for admin access..." -ForegroundColor Yellow
Write-Host ""

# Run the createsuperuser command
python manage.py createsuperuser

Write-Host ""
Write-Host "✅ Superuser created successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "📍 Access admin panel at: http://127.0.0.1:8000/admin/" -ForegroundColor Cyan
Write-Host ""
Write-Host "📖 Read ADMIN_GUIDE.md for complete admin documentation" -ForegroundColor Yellow
