from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'value_practiced', 'date', 'student_count', 'is_upcoming']
    list_filter = ['value_practiced', 'date']
    search_fields = ['title', 'description', 'value_practiced']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Activity Details', {
            'fields': ('title', 'description', 'value_practiced')
        }),
        ('Schedule & Participation', {
            'fields': ('date', 'student_count')
        }),
        ('Media', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_past', 'mark_as_upcoming']
    
    def is_upcoming(self, obj):
        from django.utils import timezone
        return obj.date >= timezone.now().date()
    is_upcoming.boolean = True
    is_upcoming.short_description = 'Upcoming'
    
    def mark_as_past(self, request, queryset):
        from django.utils import timezone
        from datetime import timedelta
        queryset.update(date=timezone.now().date() - timedelta(days=7))
        self.message_user(request, f"{queryset.count()} activities marked as past.")
    mark_as_past.short_description = "Mark as past activities"
    
    def mark_as_upcoming(self, request, queryset):
        from django.utils import timezone
        from datetime import timedelta
        queryset.update(date=timezone.now().date() + timedelta(days=7))
        self.message_user(request, f"{queryset.count()} activities marked as upcoming.")
    mark_as_upcoming.short_description = "Mark as upcoming activities"
