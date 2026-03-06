from django.db import models

class NewsUpdate(models.Model):
    ICON_CHOICES = [
        ('update', 'Update Icon (Circle)'),
        ('event', 'Event Icon (Calendar)'),
        ('voice', 'Voice Icon (Speaker)'),
        ('heart', 'Heart Icon'),
    ]
    text = models.CharField(max_length=255)
    icon_type = models.CharField(max_length=20, choices=ICON_CHOICES, default='update')
    link = models.CharField(max_length=255, blank=True, help_text="Optional URL to link to")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.text

class CoreValue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=10, help_text="Emoji or Icon code", default="🤝")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class ValueExample(models.Model):
    core_value = models.ForeignKey(CoreValue, related_name='examples', on_delete=models.CASCADE)
    level = models.CharField(max_length=50, choices=[
        ('Family', 'Family'),
        ('College', 'College'),
        ('Society', 'Society'),
        ('Profession', 'Profession')
    ])
    text = models.TextField()

    def __str__(self):
        return f"{self.core_value.name} - {self.level}"
