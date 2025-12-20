from django.db import models
from django.conf import settings

class StudentVoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name_display = models.CharField(max_length=100, help_text="Name to display (e.g. 'Anonymous' or real name)")
    content = models.TextField(help_text="Short reflection (100-150 words)")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voice by {self.name_display} - Approved: {self.is_approved}"
