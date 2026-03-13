import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')

application = get_wsgi_application()

# If using in-memory fallback on Vercel, run migrations at runtime
if os.environ.get('VERCEL'):
    from django.conf import settings
    if settings.DATABASES['default']['NAME'] == ':memory:':
        from django.core.management import call_command
        try:
            call_command('migrate', '--noinput')
        except Exception:
            pass

app = application
