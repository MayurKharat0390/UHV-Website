from django.db import models

class Quote(models.Model):
    text = models.TextField(help_text="The inspirational quote")
    author = models.CharField(max_length=200, help_text="Author or source")
    category = models.CharField(max_length=100, choices=[
        ('integrity', 'Integrity'),
        ('responsibility', 'Responsibility'),
        ('trust', 'Trust'),
        ('respect', 'Respect'),
        ('harmony', 'Harmony'),
        ('general', 'General'),
    ], default='general')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.text[:50]}... - {self.author}"
