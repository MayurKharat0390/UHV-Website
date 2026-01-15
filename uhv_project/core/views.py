from django.shortcuts import render
from innovations.models import Innovation

def home(request):
    featured_innovations = Innovation.objects.filter(is_featured=True)[:3]
    values = [
        {
            'name': 'Responsibility',
            'desc': 'Fulfilling one’s duty with care and dedication.',
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
        'featured_innovations': featured_innovations
    })
