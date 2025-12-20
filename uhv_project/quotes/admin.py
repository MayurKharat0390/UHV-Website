from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'author', 'category', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['text', 'author']
    list_editable = ['is_active']
    
    def text_preview(self, obj):
        return obj.text[:75] + '...' if len(obj.text) > 75 else obj.text
    text_preview.short_description = 'Quote'
