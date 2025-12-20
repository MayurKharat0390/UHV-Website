import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from reflections.models import ReflectionScenario

# Check scenarios
scenarios = ReflectionScenario.objects.all()
print(f"Total scenarios: {scenarios.count()}")

for s in scenarios:
    print(f"\nScenario: {s.title}")
    print(f"Options count: {s.options.count()}")
    for opt in s.options.all():
        print(f"  - {opt.option_text}")
