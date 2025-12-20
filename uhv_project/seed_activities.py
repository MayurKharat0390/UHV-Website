import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from activities.models import Activity
from datetime import date, timedelta

# Clear existing activities
Activity.objects.all().delete()

# Create sample activities
activities_data = [
    {
        'title': 'Community Clean-Up Drive',
        'value_practiced': 'Responsibility',
        'date': date.today() + timedelta(days=7),
        'student_count': 45,
        'description': 'Students organized a campus-wide cleanliness drive, demonstrating responsibility towards their environment. Teams worked together to clean common areas, plant trees, and create awareness about waste management.'
    },
    {
        'title': 'Cultural Harmony Festival',
        'value_practiced': 'Respect',
        'date': date.today() - timedelta(days=14),
        'student_count': 120,
        'description': 'A celebration of diversity where students from different backgrounds shared their cultures through music, dance, and food. This event promoted mutual respect and understanding among the student community.'
    },
    {
        'title': 'Truth & Ethics Workshop',
        'value_practiced': 'Integrity',
        'date': date.today() - timedelta(days=7),
        'student_count': 60,
        'description': 'Interactive workshop on academic integrity and ethical decision-making. Students participated in case studies and group discussions about maintaining honesty in academic and personal life.'
    },
    {
        'title': 'Peer Mentoring Program',
        'value_practiced': 'Compassion',
        'date': date.today() + timedelta(days=3),
        'student_count': 80,
        'description': 'Senior students volunteered to mentor juniors, helping them adjust to college life. This program fostered a culture of care and support within the student community.'
    },
    {
        'title': 'Team Building Workshop',
        'value_practiced': 'Harmony',
        'date': date.today() - timedelta(days=21),
        'student_count': 95,
        'description': 'Students engaged in collaborative activities designed to build trust and teamwork. The workshop emphasized the importance of working together harmoniously to achieve common goals.'
    },
]

created_count = 0
for activity_data in activities_data:
    activity = Activity.objects.create(**activity_data)
    created_count += 1
    print(f"✅ Created: {activity.title} - {activity.value_practiced}")

print(f"\n🎉 Successfully created {created_count} activities!")
print(f"📊 Total activities in database: {Activity.objects.count()}")
