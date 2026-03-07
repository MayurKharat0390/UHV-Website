from django.contrib import admin
from .models import StudentVoice

@admin.register(StudentVoice)
class StudentVoiceAdmin(admin.ModelAdmin):
    list_display = ('name_display', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    actions = ['approve_stories']

    def approve_stories(self, request, queryset):
        queryset.update(is_approved=True)
    approve_stories.short_description = 'Approve selected stories'
