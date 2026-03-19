import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from innovations.models import Innovation

def seed_innovations():
    projects = [
        {
            'title': 'Harmony Hub Mobile App',
            'short_description': 'A daily mindfulness and values-tracking app for students.',
            'description': 'Harmony Hub is a comprehensive mobile application designed to help students integrate UHV principles into their daily lives. It features a mood tracker, values-based decision-making tool, and a community reflection board.',
            'innovation_type': 'app',
            'developed_by': 'Amit Sharma (CSE 3rd Year) & Dr. R. K. Singh',
            'link': 'https://harmonyhub.example.com',
            'is_featured': True,
            'thumbnail': 'innovations/thumbnails/wellness_hub.png'
        },
        {
            'title': 'UHV Impact Portal',
            'short_description': 'A data-driven platform tracking UHV implementation across colleges.',
            'description': 'A web portal that aggregates impact data from various institutions implementing UHV curricula. It provides visual insights into student well-being and campus culture improvements.',
            'innovation_type': 'website',
            'developed_by': 'Priya Das (IT) & Faculty Mentors',
            'link': 'https://impact.uhv.example.com',
            'is_featured': True,
            'thumbnail': 'innovations/thumbnails/shareplate.png'
        },
        {
            'title': 'Ethical Dilemma Simulator',
            'short_description': 'Interactive scenarios for practicing ethical decision-making.',
            'description': 'A web-based tool where users can navigate complex ethical scenarios. Each choice is mapped to core human values, providing immediate feedback on the impact of decisions.',
            'innovation_type': 'tool',
            'developed_by': 'Siddharth Varma (Software Eng) & UHV Faculty',
            'link': 'https://ethics.sim.example.com',
            'is_featured': True
        },
        {
            'title': 'LifeSync 2.0',
            'short_description': 'Harmony and balance ecosystem for holistic human values integration.',
            'description': 'LifeSync 2.0 is an advanced web portal designed to integrate core human values into modern daily life. It features mindfulness tools, relationship management scenarios, and personal value tracking.',
            'innovation_type': 'website',
            'developed_by': 'UHV Innovation Lab',
            'link': 'https://life-sync2-0.vercel.app/',
            'is_featured': True,
            'thumbnail': 'innovations/thumbnails/lifesync_2_0.png'
        }
    ]

    for p in projects:
        innovation_defaults = {
            'short_description': p['short_description'],
            'description': p['description'],
            'innovation_type': p['innovation_type'],
            'developed_by': p['developed_by'],
            'link': p['link'],
            'is_featured': p['is_featured']
        }
        if 'thumbnail' in p:
            innovation_defaults['thumbnail'] = p['thumbnail']

        innovation, created = Innovation.objects.get_or_create(
            title=p['title'],
            defaults=innovation_defaults
        )
        if created:
            print(f"Created: {p['title']}")
        else:
            print(f"Already exists: {p['title']}")

if __name__ == '__main__':
    seed_innovations()
