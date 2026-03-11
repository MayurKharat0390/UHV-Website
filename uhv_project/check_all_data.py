import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from innovations.models import Innovation
from voices.models import Voice
from faculty.models import FacultyProfile

print(f"Innovations: {[i.title for i in Innovation.objects.all()]}")
print(f"Voices: {[v.title for v in Voice.objects.all() if hasattr(v, 'title')] or [v.id for v in Voice.objects.all()]}")
print(f"Faculty: {[f.name for f in FacultyProfile.objects.all()]}")
