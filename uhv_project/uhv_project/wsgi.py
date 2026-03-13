import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to path so settings can be imported
# This handles the nested folder structure for Vercel
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')

application = get_wsgi_application()

# If using in-memory fallback on Vercel, run migrations at runtime
if os.environ.get('VERCEL'):
    from django.conf import settings
    try:
        if settings.DATABASES['default']['NAME'] == ':memory:':
            from django.core.management import call_command
            call_command('migrate', '--noinput')
    except Exception:
        pass

app = application
