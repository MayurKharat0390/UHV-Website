from django.db import models
from django.conf import settings

class JournalEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', '😊 Happy'),
        ('calm', '😌 Calm'),
        ('thoughtful', '🤔 Thoughtful'),
        ('grateful', '🙏 Grateful'),
        ('challenged', '💪 Challenged'),
        ('confused', '😕 Confused'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Journal Entries"
    
    def __str__(self):
        return f"Journal by {self.user} on {self.created_at.date()}"
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
