import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from voices.models import StudentVoice

# Approve all student voices
voices = StudentVoice.objects.all()
approved_count = voices.update(is_approved=True)

print(f"✅ Approved {approved_count} student voices")
print(f"📝 Total voices in database: {voices.count()}")

for voice in voices:
    print(f"  - {voice.student_name}: {voice.reflection[:50]}...")
