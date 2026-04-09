from .models import NewsUpdate
from reflections.models import ReflectionScenario
from django.utils import timezone

def news_ticker(request):
    try:
        updates = list(NewsUpdate.objects.filter(is_active=True).order_by('order', '-created_at'))
    except Exception:
        updates = []

    # Fallback to hardcoded updates if DB is empty or tables are missing
    if not updates:
        updates = [
            {'text': 'MDP on Universal Human Values inaugurated at PCCoE (8th-10th April). Organized for senior leaders.', 'icon_type': 'event'},
            {'text': '78 delegates (48 PCCoE, 31 from other institutions) participating in the 3-day MDP program.', 'icon_type': 'update'},
            {'text': 'Dignitaries: Dr. Pramod Patil, Dr. Rajeev Nargundkar, & Dr. Govind Kulkarni graced the inauguration.', 'icon_type': 'update'},
            {'text': 'AICTE UHV Cell: Dr. Umesh Jadhav (Resource Person), Dr. Anita Mane (Co-Facilitator), Ms. Kiran Naphade (Observer).', 'icon_type': 'update'},
            {'text': 'MDP focuses on Right Understanding, Right Feelings, and Right Conduct for ethical leadership.', 'icon_type': 'update'},
        ]
        
    return {
        'ticker_updates': updates
    }

def daily_reflection(request):
    try:
        today = timezone.now().date()
        
        # First, try to get a scenario specifically scheduled for today
        scenario = ReflectionScenario.objects.prefetch_related('options').filter(active_date=today).first()
        
        if not scenario:
            # No specific scenario for today - rotate through all scenarios
            all_scenarios = ReflectionScenario.objects.prefetch_related('options').all()
            
            # Force execution check
            if all_scenarios.exists():
                day_of_year = today.timetuple().tm_yday
                scenario_count = all_scenarios.count()
                scenario_index = day_of_year % scenario_count
                scenario = all_scenarios[scenario_index]
    except Exception:
        scenario = None
        
    return {
        'daily_scenario': scenario
    }

def visitor_count(request):
    try:
        from .models import SiteVisitor
        count = SiteVisitor.get_total_count()
    except Exception:
        count = 0
    return {
        'total_visitors': count
    }
