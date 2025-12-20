import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from reflections.models import ReflectionScenario, ReflectionOption

def seed():
    print("Seeding Reflection Scenarios...")
    
    # Clear existing scenarios
    ReflectionScenario.objects.all().delete()
    
    today = timezone.now().date()
    
    # Scenario 1: Found Wallet
    s1 = ReflectionScenario.objects.create(
        title="Found Wallet",
        scenario_text="You find a wallet with ID and cash in the college cafeteria. No one is watching.",
        explanation="Returning the wallet builds Trust and Integrity. It reflects a responsible self that values others' feelings over material gain. This small act creates ripples of honesty in society.",
        related_value="Integrity & Trust",
        active_date=today
    )
    ReflectionOption.objects.create(scenario=s1, option_text="Return it to the ID owner or Lost & Found immediately")
    ReflectionOption.objects.create(scenario=s1, option_text="Keep the cash and return the wallet anonymously")
    ReflectionOption.objects.create(scenario=s1, option_text="Leave it there for someone else to handle")
    ReflectionOption.objects.create(scenario=s1, option_text="Take it to campus security")
    
    # Scenario 2: Group Project
    s2 = ReflectionScenario.objects.create(
        title="Group Project Dilemma",
        scenario_text="Your group member hasn't contributed to the project. The deadline is tomorrow. What do you do?",
        explanation="True Harmony comes from addressing issues with compassion while maintaining fairness. Communication and understanding create stronger relationships than silent resentment or unfair advantage.",
        related_value="Harmony & Fairness",
        active_date=today + timedelta(days=1)
    )
    ReflectionOption.objects.create(scenario=s2, option_text="Talk to them privately to understand their situation")
    ReflectionOption.objects.create(scenario=s2, option_text="Complete their part yourself to avoid conflict")
    ReflectionOption.objects.create(scenario=s2, option_text="Report them to the professor immediately")
    ReflectionOption.objects.create(scenario=s2, option_text="Divide the work fairly and ask them to contribute now")
    
    # Scenario 3: Exam Help
    s3 = ReflectionScenario.objects.create(
        title="Exam Assistance",
        scenario_text="During an exam, your best friend asks you for an answer. The teacher isn't looking.",
        explanation="Integrity means doing the right thing even when no one is watching. Helping in dishonest ways harms both you and your friend's growth. True friendship supports honest effort.",
        related_value="Integrity & Responsibility",
        active_date=today + timedelta(days=2)
    )
    ReflectionOption.objects.create(scenario=s3, option_text="Politely refuse and focus on your own exam")
    ReflectionOption.objects.create(scenario=s3, option_text="Help them this one time since they're your friend")
    ReflectionOption.objects.create(scenario=s3, option_text="Pretend you didn't see their request")
    ReflectionOption.objects.create(scenario=s3, option_text="Signal to the teacher about the situation")
    
    # Scenario 4: Environmental Choice
    s4 = ReflectionScenario.objects.create(
        title="Campus Cleanliness",
        scenario_text="You see someone litter on campus. There's a dustbin nearby. What do you do?",
        explanation="Responsibility extends beyond our personal actions to our community. Gentle awareness-raising creates positive change. Our environment reflects our collective values.",
        related_value="Responsibility & Respect",
        active_date=today + timedelta(days=3)
    )
    ReflectionOption.objects.create(scenario=s4, option_text="Pick it up yourself and dispose it properly")
    ReflectionOption.objects.create(scenario=s4, option_text="Politely ask them to use the dustbin")
    ReflectionOption.objects.create(scenario=s4, option_text="Ignore it, it's not your responsibility")
    ReflectionOption.objects.create(scenario=s4, option_text="Report it to campus authorities")
    
    # Scenario 5: Social Media Truth
    s5 = ReflectionScenario.objects.create(
        title="Viral Misinformation",
        scenario_text="You see a viral post about your college that contains false information. It has 1000+ shares.",
        explanation="Truth and Integrity matter in the digital age. Spreading misinformation harms trust. Taking time to verify and correct builds a culture of honesty and respect for facts.",
        related_value="Truth & Integrity",
        active_date=today + timedelta(days=4)
    )
    ReflectionOption.objects.create(scenario=s5, option_text="Comment with correct information and facts")
    ReflectionOption.objects.create(scenario=s5, option_text="Share it anyway since everyone else is")
    ReflectionOption.objects.create(scenario=s5, option_text="Report the post as misinformation")
    ReflectionOption.objects.create(scenario=s5, option_text="Ignore it and scroll past")
    
    # Scenario 6: Time Management
    s6 = ReflectionScenario.objects.create(
        title="Commitment Conflict",
        scenario_text="You promised to help a junior with studies, but your friends invite you to a movie at the same time.",
        explanation="Responsibility means honoring commitments. Trust is built through reliability. Respecting others' time and needs creates harmony in relationships.",
        related_value="Responsibility & Trust",
        active_date=today + timedelta(days=5)
    )
    ReflectionOption.objects.create(scenario=s6, option_text="Keep your promise and help the junior")
    ReflectionOption.objects.create(scenario=s6, option_text="Reschedule with the junior for another day")
    ReflectionOption.objects.create(scenario=s6, option_text="Go to the movie and apologize later")
    ReflectionOption.objects.create(scenario=s6, option_text="Ask friends to postpone the movie")
    
    # Scenario 7: Diversity & Inclusion
    s7 = ReflectionScenario.objects.create(
        title="New Student Welcome",
        scenario_text="A new student from a different state joins your class. They seem shy and sit alone during lunch.",
        explanation="Respect and Harmony grow when we embrace diversity. Small acts of inclusion create belonging. Everyone deserves to feel welcomed and valued.",
        related_value="Respect & Harmony",
        active_date=today + timedelta(days=6)
    )
    ReflectionOption.objects.create(scenario=s7, option_text="Invite them to join your lunch group")
    ReflectionOption.objects.create(scenario=s7, option_text="Smile and wave but let them adjust on their own")
    ReflectionOption.objects.create(scenario=s7, option_text="Wait for them to approach you first")
    ReflectionOption.objects.create(scenario=s7, option_text="Introduce them to other friendly classmates")
    
    print(f"✅ Created 7 reflection scenarios with options!")
    print(f"📅 Scenarios scheduled from {today} to {today + timedelta(days=6)}")

if __name__ == "__main__":
    seed()
