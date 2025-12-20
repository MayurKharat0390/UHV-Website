from django.db import models

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('pdf', 'PDF Document'),
        ('link', 'External Link'),
    ]
    
    title = models.CharField(max_length=300)
    description = models.TextField()
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    url = models.URLField(blank=True, null=True, help_text="External link or video URL")
    file = models.FileField(upload_to='resources/', blank=True, null=True, help_text="Upload PDF or document")
    category = models.CharField(max_length=100, choices=[
        ('integrity', 'Integrity'),
        ('responsibility', 'Responsibility'),
        ('trust', 'Trust'),
        ('respect', 'Respect'),
        ('harmony', 'Harmony'),
        ('general', 'General'),
    ], default='general')
    thumbnail = models.ImageField(upload_to='resource_thumbnails/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', '-created_at']
    
    def __str__(self):
        return f"{self.title} ({self.get_resource_type_display()})"
