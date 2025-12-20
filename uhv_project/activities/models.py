from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    value_practiced = models.CharField(max_length=100)
    student_count = models.PositiveIntegerField(help_text="Number of students involved")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='activities/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title
