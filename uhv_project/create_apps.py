# Create new apps
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from django.core.management import call_command

# Create new apps
apps = ['quotes', 'resources', 'progress']

for app in apps:
    try:
        call_command('startapp', app)
        print(f"✅ Created {app} app")
    except Exception as e:
        print(f"⚠️  {app} app may already exist: {e}")
