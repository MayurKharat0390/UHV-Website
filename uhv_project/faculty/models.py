from django.db import models

class FacultyProfile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    philosophy = models.CharField(max_length=200, help_text="One-line philosophy on values")
    image = models.ImageField(upload_to='faculty/', blank=True, null=True)

    def __str__(self):
        return self.name
