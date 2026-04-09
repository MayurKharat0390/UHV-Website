import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from core.models import NewsUpdate
from activities.models import Activity
from datetime import date

def add_mdp_updates():
    # 1. Add Ticker Updates
    updates = [
        {
            'text': 'MDP on Universal Human Values inaugurated at PCCoE (8th-10th April). 🏛️',
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
    
    for item in updates:
        NewsUpdate.objects.get_or_create(
            text=item['text'],
            defaults={
                'icon_type': item['icon_type'],
                'order': item['order'],
                'is_active': True
            }
        )
        clean_text = item['text'].encode('ascii', 'ignore').decode('ascii')
        print(f"Added/Updated ticker: {clean_text}")

    # 2. Add Activity Entry
    mdp_desc = """The Management Development Program (MDP) on Universal Human Values was successfully inaugurated today at Pimpri Chinchwad College of Engineering (PCCoE). 
Organized from 8th to 10th April, this program brings together senior leaders from various institutions with a shared vision of fostering value-based education, ethical leadership, and holistic growth.

The inaugural session was graced by esteemed dignitaries including Dr. Pramod Patil (Dean, Savitribai Phule Pune University & Director, NMIET), Dr. Rajeev Nargundkar, and Dr. Govind Kulkarni (Director, PCCoE). We are also privileged to have the guidance and presence of the AICTE Universal Human Values Cell team  Dr. Umesh Jadhav (Resource Person), Dr. Anita Mane (Co-Facilitator), and Ms. Kiran Naphade (Observer).

Day 1 witnessed enthusiastic participation from 78 delegates, including 48 from PCCoE and 31 from other institutions, highlighting a rich diversity of perspectives and active engagement.
The program emphasizes developing right understanding, right feelings, and right conduct, while promoting ethics, social responsibility, and value-based education. It serves as a meaningful platform for dialogue, reflection, and collaborative learningreinforcing that true excellence lies in the integration of competence with character."""

    Activity.objects.get_or_create(
        title="MDP on Universal Human Values",
        date=date(2026, 4, 8),
        defaults={
            'value_practiced': "Ethical Leadership & Right Conduct",
            'student_count': 78,
            'description': mdp_desc
        }
    )
    print("Added/Updated Activity: MDP on Universal Human Values")

if __name__ == "__main__":
    add_mdp_updates()
