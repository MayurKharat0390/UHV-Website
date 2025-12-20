from django.utils import timezone
from datetime import timedelta

class LoginStreakMiddleware:
    """
    Middleware to track user logins and calculate streaks.
    Runs on every request for authenticated users.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request
        if request.user.is_authenticated:
            self.track_login(request.user)
        
        response = self.get_response(request)
        return response

    def track_login(self, user):
        """Track user login and update streak"""
        from progress.models import UserProgress, LoginStreak
        
        today = timezone.now().date()
        
        # Get or create user progress
        progress, created = UserProgress.objects.get_or_create(user=user)
        
        # Check if already logged in today
        login_streak, created = LoginStreak.objects.get_or_create(
            user=user,
            date=today,
            defaults={'login_count': 1}
        )
        
        # If not created (already exists), increment login count
        if not created:
            login_streak.login_count += 1
            login_streak.save()
        else:
            # First login of the day - increment total logins
            progress.total_logins += 1
        
        # Update last login date
        progress.last_login_date = today
        
        # Calculate current streak
        current_streak = self.calculate_streak(user, today)
        progress.current_streak = current_streak
        
        # Update longest streak if current is better
        if current_streak > progress.longest_streak:
            progress.longest_streak = current_streak
        
        progress.save()

    def calculate_streak(self, user, today):
        """Calculate consecutive login days"""
        from progress.models import LoginStreak
        
        streak = 0
        check_date = today
        
        # Count backwards from today
        while True:
            if LoginStreak.objects.filter(user=user, date=check_date).exists():
                streak += 1
                check_date -= timedelta(days=1)
            else:
                break
        
        return streak
