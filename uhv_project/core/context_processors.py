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
            {'text': 'Welcome to the PCCOE Institute UHV Cell! 🌟', 'icon_type': 'update'},
            {'text': 'New Session on Universal Human Values starting soon. 🏛️', 'icon_type': 'event'},
            {'text': 'Digital UHV Innovations now showcase student leadership. 💻', 'icon_type': 'update'},
            {'text': 'Connect with our UHV Cell for holistic development. 🤝', 'icon_type': 'event'}
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
