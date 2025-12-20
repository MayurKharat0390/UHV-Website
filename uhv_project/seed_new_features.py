import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from quotes.models import Quote
from resources.models import Resource

print("Seeding Quotes...")

quotes_data = [
    {"text": "The best way to find yourself is to lose yourself in the service of others.", "author": "Mahatma Gandhi", "category": "responsibility"},
    {"text": "Integrity is doing the right thing, even when no one is watching.", "author": "C.S. Lewis", "category": "integrity"},
    {"text": "Trust is built with consistency.", "author": "Lincoln Chafee", "category": "trust"},
    {"text": "Respect for ourselves guides our morals; respect for others guides our manners.", "author": "Laurence Sterne", "category": "respect"},
    {"text": "Harmony makes small things grow, lack of it makes great things decay.", "author": "Sallust", "category": "harmony"},
    {"text": "Education is the most powerful weapon which you can use to change the world.", "author": "Nelson Mandela", "category": "general"},
    {"text": "Be the change you wish to see in the world.", "author": "Mahatma Gandhi", "category": "responsibility"},
    {"text": "Character is like a tree and reputation like a shadow. The shadow is what we think of it; the tree is the real thing.", "author": "Abraham Lincoln", "category": "integrity"},
    {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela", "category": "general"},
    {"text": "In a gentle way, you can shake the world.", "author": "Mahatma Gandhi", "category": "harmony"},
]

Quote.objects.all().delete()
for quote_data in quotes_data:
    Quote.objects.create(**quote_data)

print(f"✅ Created {len(quotes_data)} quotes")

print("\nSeeding Resources...")

resources_data = [
    {
        "title": "Introduction to Universal Human Values",
        "description": "A comprehensive guide to understanding the core principles of UHV and their application in daily life.",
        "resource_type": "article",
        "category": "general",
        "is_featured": True,
    },
    {
        "title": "The Power of Ethical Living",
        "description": "Explore how ethical decisions shape our character and influence society positively.",
        "resource_type": "article",
        "category": "integrity",
        "is_featured": True,
    },
    {
        "title": "Building Trust in Relationships",
        "description": "Learn practical strategies for developing and maintaining trust in personal and professional relationships.",
        "resource_type": "article",
        "category": "trust",
    },
]

Resource.objects.all().delete()
for resource_data in resources_data:
    Resource.objects.create(**resource_data)

print(f"✅ Created {len(resources_data)} resources")
print("\n🎉 All seed data created successfully!")
