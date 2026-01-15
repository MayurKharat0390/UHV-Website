from django.db import models

class Innovation(models.Model):
    INNOVATION_TYPES = [
        ('app', 'Mobile Application'),
        ('website', 'Website/Portal'),
        ('tool', 'Digital Tool'),
        ('research', 'Research Project'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(help_text="Detailed information about the project")
    short_description = models.CharField(max_length=250, help_text="A brief summary for the thumbnail")
    thumbnail = models.ImageField(upload_to='innovations/thumbnails/')
    innovation_type = models.CharField(max_length=20, choices=INNOVATION_TYPES, default='website')
    developed_by = models.CharField(max_length=300, help_text="Names of students/faculty involved")
    link = models.URLField(help_text="Direct link to the project/website")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']
        verbose_name = "UHV Innovation"
        verbose_name_plural = "UHV Innovations"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
