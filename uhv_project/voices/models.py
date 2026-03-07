from django.db import models
from django.conf import settings

class StudentVoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name_display = models.CharField(max_length=100, help_text="Name to display (e.g. 'Anonymous' or real name)")
    content = models.TextField(help_text="Short story of change (100-150 words)")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Impact Story"
        verbose_name_plural = "Impact Stories"

    def __str__(self):
        return f"Impact Story by {self.name_display} - Approved: {self.is_approved} "

class StoryMedia(models.Model):
    story = models.ForeignKey(StudentVoice, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='story_media/', help_text="Upload photo or video")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def is_image(self):
        ext = self.file.name.split('.')[-1].lower()
        return ext in ['jpg', 'jpeg', 'png', 'gif', 'webp']

    def is_video(self):
        ext = self.file.name.split('.')[-1].lower()
        return ext in ['mp4', 'mov', 'avi', 'webm']

    def __str__(self):
        return f"Media for {self.story.name_display}"
