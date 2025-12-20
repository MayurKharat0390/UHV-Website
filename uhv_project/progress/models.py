from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    total_reflections = models.IntegerField(default=0)
    total_logins = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_login_date = models.DateField(null=True, blank=True)
    last_reflection_date = models.DateField(null=True, blank=True)
    total_journal_entries = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "User Progress"
    
    def __str__(self):
        return f"{self.user.username}'s Progress"

class LoginStreak(models.Model):
    """Track daily logins for streak calculation"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_streaks')
    date = models.DateField()
    login_count = models.IntegerField(default=1)  # How many times logged in that day
    
    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.user.username} - {self.date} ({self.login_count} logins)"

class ReflectionStreak(models.Model):
    """Track daily reflections (kept for compatibility)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reflection_streaks')
    date = models.DateField()
    reflection_completed = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"
