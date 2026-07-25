from django.db import models

class CoreValue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=10, default="🤝", help_text="Emoji or Icon code")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class ValueExample(models.Model):
    LEVEL_CHOICES = [
        ('Family', 'Family'),
        ('College', 'College'),
        ('Society', 'Society'),
        ('Profession', 'Profession'),
    ]
    core_value = models.ForeignKey(CoreValue, related_name='examples', on_delete=models.CASCADE)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    text = models.TextField()

    def __str__(self):
        return f"{self.core_value.name} - {self.level}"

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

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class SiteVisitor(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    last_visit = models.DateTimeField(auto_now=True)
    visit_count = models.PositiveIntegerField(default=1)

    @classmethod
    def get_total_count(cls):
        from django.db.models import Sum
        return cls.objects.aggregate(total=Sum('visit_count'))['total'] or 0

    def __str__(self):
        return f"{self.ip_address} - {self.last_visit}"
