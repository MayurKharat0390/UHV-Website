import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from innovations.models import Innovation

def seed_innovations():
    # Clear existing innovations to remove dummy data
    print("🗑️ Clearing existing innovations...")
    Innovation.objects.all().delete()

    projects = [
        {
            'title': 'LifeSync 2.0',
            'short_description': 'Advanced Harmony and Life-Balance Ecosystem.',
            'description': 'LifeSync 2.0 is an advanced platform designed to integrate core human values into modern daily life through mindfulness, relationship harmony, and value tracking.',
            'innovation_type': 'website',
            'developed_by': 'UHV Innovation Team',
            'link': 'https://life-sync2-0.vercel.app/',
            'is_featured': True,
            'thumbnail': 'innovations/thumbnails/lifesync_2_0.png'
        },
        {
            'title': 'SharePlate',
            'short_description': 'A community platform for food sharing and reducing waste.',
            'description': 'SharePlate connects community members to share surplus food, fostering harmony and responsibility towards the environment and society.',
            'innovation_type': 'website',
            'developed_by': 'UHV Student Developers',
            'link': 'https://sharing-plate.vercel.app/',
            'is_featured': True,
            'thumbnail': 'innovations/thumbnails/shareplate.png'
        },
        {
            'title': 'Wellness Hub',
            'short_description': 'Mindfulness and values-based wellness for students.',
            'description': 'Wellness Hub provides interactive tools for self-exploration, stress management, and tracking personal growth based on Universal Human Values.',
            'innovation_type': 'tool',
            'developed_by': 'UHV Wellness Cell',
            'link': 'https://uhv.najrudin.com.np/',
            'is_featured': True,
            'thumbnail': 'innovations/thumbnails/wellness_hub.png'
        }
    ]

    for p in projects:
        innovation, created = Innovation.objects.update_or_create(
            title=p['title'],
            defaults={
                'short_description': p['short_description'],
                'description': p['description'],
                'innovation_type': p['innovation_type'],
                'developed_by': p['developed_by'],
                'link': p['link'],
                'is_featured': p['is_featured'],
                'thumbnail': p['thumbnail']
            }
        )
        print(f"✅ Seeding: {p['title']} ({'Created' if created else 'Updated'})")

    print("\n🚀 All real innovations seeded successfully!")

if __name__ == '__main__':
    seed_innovations()
