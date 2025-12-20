from django.contrib import admin
from .models import JournalEntry

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'mood_display', 'word_count', 'created_at', 'has_tags']
    list_filter = ['mood', 'created_at']
    search_fields = ['user__username', 'content', 'tags']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at', 'word_count']
    
    fieldsets = (
        ('User & Metadata', {
            'fields': ('user', 'mood', 'tags')
        }),
        ('Content', {
            'fields': ('content',),
            'classes': ('wide',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def mood_display(self, obj):
        return obj.get_mood_display() if obj.mood else '-'
    mood_display.short_description = 'Mood'
    
    def word_count(self, obj):
        return len(obj.content.split())
    word_count.short_description = 'Words'
    
    def has_tags(self, obj):
        return bool(obj.tags)
    has_tags.boolean = True
    has_tags.short_description = 'Tagged'
