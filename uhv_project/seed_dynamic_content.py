import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from core.models import NewsUpdate, CoreValue, ValueExample

def seed():
    # News Updates
    NewsUpdate.objects.all().delete()
    updates = [
        ('NEW REFLECTION SCENARIO: THE EXAM DILEMMA – NOW LIVE FOR 2026!', 'update', 1),
        ('UPCOMING WORKSHOP: ETHICAL LIVING IN DIGITAL AGE – MARCH 25TH.', 'event', 2),
        ('STUDENT SPOTLIGHT: "HOW INTEGRITY SHAPES SUCCESS" – READ MORE IN VOICES.', 'voice', 3),
        ('JOIN THE COMMUNITY: SHARE YOUR PERSPECTIVE ON HUMAN VALUES TODAY.', 'heart', 4),
    ]
    for text, icon, order in updates:
        NewsUpdate.objects.create(text=text, icon_type=icon, order=order)
    print(f"Seeded {NewsUpdate.objects.count()} news updates.")

    # Core Values
    CoreValue.objects.all().delete()
    values_data = [
        {
            'name': 'Responsibility',
            'desc': 'Fulfilling one’s duty with care and dedication.',
            'icon': '🤝',
            'order': 1,
            'examples': {
                'Family': 'Taking care of parents.',
                'College': 'Submitting assignments on time.',
                'Society': 'Following traffic rules.',
                'Profession': 'Meeting project deadlines.'
            }
        },
        {
            'name': 'Trust',
            'desc': 'Assurance in the intention of the other.',
            'icon': '🌟',
            'order': 2,
            'examples': {
                'Family': 'Believing in siblings.',
                'College': 'Avoiding plagiarism.',
                'Society': 'Honest transactions.',
                'Profession': 'Keeping client data confidential.'
            }
        }
    ]
    for v_data in values_data:
        v = CoreValue.objects.create(
            name=v_data['name'],
            description=v_data['desc'],
            icon=v_data['icon'],
            order=v_data['order']
        )
        for level, text in v_data['examples'].items():
            ValueExample.objects.create(core_value=v, level=level, text=text)
    print(f"Seeded {CoreValue.objects.count()} core values.")

if __name__ == '__main__':
    seed()
