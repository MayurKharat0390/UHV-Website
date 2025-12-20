from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'resource_type', 'category', 'is_featured', 'views_count', 'created_at']
    list_filter = ['resource_type', 'category', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']
    readonly_fields = ['views_count', 'created_at', 'updated_at']
