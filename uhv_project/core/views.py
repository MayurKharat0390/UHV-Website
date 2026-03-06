from django.shortcuts import render
from innovations.models import Innovation
from faculty.models import FacultyProfile
from .models import NewsUpdate, CoreValue

def home(request):
    featured_innovations = Innovation.objects.filter(is_featured=True)[:3]
    faculties = FacultyProfile.objects.all()
    
    # Dynamic values from DB
    db_values = CoreValue.objects.all().prefetch_related('examples')
    values = []
    
    for v in db_values:
        example_dict = {ex.level: ex.text for ex in v.examples.all()}
        values.append({
            'name': v.name,
            'desc': v.description,
            'icon': v.icon,
            'examples': example_dict
        })

    # Fallback to hardcoded if DB is empty to prevent breakages during setup
    if not values:
        values = [
            {
                'name': 'Responsibility',
                'desc': 'Fulfilling one’s duty with care and dedication.',
                'icon': '🤝',
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
                'examples': {
                    'Family': 'Believing in siblings.',
                    'College': 'Avoiding plagiarism.',
                    'Society': 'Honest transactions.',
                    'Profession': 'Keeping client data confidential.'
                }
            },
            {
                'name': 'Respect',
                'desc': 'Right evaluation of oneself and others.',
                'icon': '💚',
                'examples': {
                    'Family': 'Listening to elders.',
                    'College': 'Respecting teachers and peers.',
                    'Society': 'No discrimination.',
                    'Profession': 'Valuing colleagues’ time.'
                }
            },
            {
                'name': 'Harmony',
                'desc': 'Co-existence and mutual fulfillment.',
                'icon': '🎯',
                'examples': {
                    'Family': 'Spending quality time.',
                    'College': 'Group study and help.',
                    'Society': 'Community service.',
                    'Profession': 'Work-life balance.'
                }
            }
        ]

    return render(request, 'core/home.html', {
        'values': values,
        'featured_innovations': featured_innovations,
        'faculties': faculties,
    })
