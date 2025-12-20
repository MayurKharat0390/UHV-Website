from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import ReflectionScenario, ReflectionOption, UserResponse
from django.views.decorators.http import require_POST

def daily_reflection(request):
    """
    Get today's reflection scenario.
    Rotates through all scenarios automatically - different one each day!
    """
    from datetime import datetime
    
    today = timezone.now().date()
    
    # First, try to get a scenario specifically scheduled for today
    scenario = ReflectionScenario.objects.prefetch_related('options').filter(active_date=today).first()
    
    if not scenario:
        # No specific scenario for today - rotate through all scenarios
        all_scenarios = ReflectionScenario.objects.prefetch_related('options').all()
        
        if all_scenarios.exists():
            # Calculate which scenario to show based on day of year
            # This ensures same scenario shows for everyone on the same day
            day_of_year = today.timetuple().tm_yday
            scenario_count = all_scenarios.count()
            scenario_index = day_of_year % scenario_count
            
            scenario = all_scenarios[scenario_index]
        else:
            scenario = None
    
    # Debug: Print to console
    if scenario:
        print(f"📅 Today's Scenario ({today}): {scenario.title}")
        print(f"Options:")
        for opt in scenario.options.all():
            print(f"  Option {opt.id}: {opt.option_text}")
    else:
        print("⚠️ No scenario found! Please add scenarios via admin.")
    
    # Use debug template if ?debug=1 in URL
    if request.GET.get('debug'):
        return render(request, 'reflections/debug.html', {'scenario': scenario})
    
    context = {'scenario': scenario}
    return render(request, 'reflections/daily_card.html', context)

@require_POST
def submit_reflection(request, scenario_id):
    from django.utils import timezone
    from django.contrib import messages
    
    scenario = get_object_or_404(ReflectionScenario, pk=scenario_id)
    option_id = request.POST.get('option')
    option = get_object_or_404(ReflectionOption, pk=option_id)
    
    # Store response (anonymous if not logged in, or linked)
    user = request.user if request.user.is_authenticated else None
    
    # Check if user already submitted a reflection today
    if user:
        today = timezone.now().date()
        already_reflected_today = UserResponse.objects.filter(
            user=user,
            created_at__date=today
        ).exists()
        
        if already_reflected_today:
            messages.warning(request, "You've already completed your reflection for today! Come back tomorrow. 🌟")
            return render(request, 'reflections/already_completed.html', {
                'scenario': scenario,
                'message': "You've already reflected today!"
            })
    
    # Create the response
    UserResponse.objects.create(
        user=user,
        scenario=scenario,
        selected_option=option
    )
    
    # Update progress and streak for logged-in users
    if user:
        from progress.models import UserProgress, ReflectionStreak
        
        today = timezone.now().date()
        
        # Mark today's reflection as complete
        ReflectionStreak.objects.update_or_create(
            user=user,
            date=today,
            defaults={'reflection_completed': True}
        )
        
        # Update user progress
        progress, created = UserProgress.objects.get_or_create(user=user)
        progress.total_reflections = UserResponse.objects.filter(user=user).count()
        progress.last_reflection_date = today
        progress.save()
    
    return render(request, 'reflections/feedback.html', {'scenario': scenario, 'selected_option': option})
