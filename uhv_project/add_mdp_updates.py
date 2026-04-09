import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from core.models import NewsUpdate

def add_mdp_updates():
    updates = [
        {
            'text': 'MDP on Universal Human Values successfully inaugurated at PCCoE (8th-10th April). 🏛️',
            'icon_type': 'event',
            'order': 1
        },
        {
            'text': '78 delegates (48 PCCoE, 31 Guests) exploring Value-Based Education in MDP Day 1. 🤝',
            'icon_type': 'update',
            'order': 2
        },
        {
            'text': 'Esteemed Dignitaries: Dr. Pramod Patil, Dr. Rajeev Nargundkar, & Dr. Govind Kulkarni at MDP. 🌟',
            'icon_type': 'update',
            'order': 3
        },
        {
            'text': 'Expert Guidance from AICTE UHV Cell: Dr. Umesh Jadhav, Dr. Anita Mane, & Ms. Kiran Naphade. 🧭',
            'icon_type': 'update',
            'order': 4
        }
    ]
    
    # Optional: Deactivate old updates if count is getting too high
    # NewsUpdate.objects.all().update(is_active=False)
    
    for item in updates:
        # DB usually handles UTF-8, but shell might not
        NewsUpdate.objects.create(
            text=item['text'],
            icon_type=item['icon_type'],
            order=item['order'],
            is_active=True
        )
        # Filter out non-ascii for print
        clean_text = item['text'].encode('ascii', 'ignore').decode('ascii')
        print(f"Added update: {clean_text}")

if __name__ == "__main__":
    add_mdp_updates()
