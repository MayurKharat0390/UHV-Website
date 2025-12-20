from django.contrib import admin
from .models import StudentVoice

@admin.register(StudentVoice)
class StudentVoiceAdmin(admin.ModelAdmin):
    list_display = ('name_display', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    actions = ['approve_voices']

    def approve_voices(self, request, queryset):
        queryset.update(is_approved=True)
