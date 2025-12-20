from django.db import models
from django.conf import settings
from django.utils import timezone

class ReflectionScenario(models.Model):
    title = models.CharField(max_length=200)
    scenario_text = models.TextField()
    explanation = models.TextField(help_text="Reflective explanation shown after selection")
    related_value = models.CharField(max_length=100, default='Responsibility')
    active_date = models.DateField(default=timezone.now, unique=True, help_text="Date this scenario is active")

    def __str__(self):
        return f"{self.active_date} - {self.title}"

class ReflectionOption(models.Model):
    scenario = models.ForeignKey(ReflectionScenario, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=300)

    def __str__(self):
        return self.option_text

class UserResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    scenario = models.ForeignKey(ReflectionScenario, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(ReflectionOption, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.scenario} by {self.user}"
