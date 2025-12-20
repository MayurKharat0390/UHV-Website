from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProgress, LoginStreak
from reflections.models import UserResponse
from journals.models import JournalEntry
from django.utils import timezone
from datetime import timedelta

@login_required
def dashboard(request):
    # Get or create user progress
    progress, created = UserProgress.objects.get_or_create(user=request.user)
    
    # Update stats
    progress.total_reflections = UserResponse.objects.filter(user=request.user).count()
    progress.total_journal_entries = JournalEntry.objects.filter(user=request.user).count()
    progress.save()
    
    # Get last 30 days of login activity
    thirty_days_ago = timezone.now().date() - timedelta(days=30)
    recent_logins = LoginStreak.objects.filter(
        user=request.user,
        date__gte=thirty_days_ago
    ).order_by('date')
    
    context = {
        'progress': progress,
        'recent_logins': recent_logins,
    }
    return render(request, 'progress/dashboard.html', context)
