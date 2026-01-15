from django.contrib import admin
from .models import Innovation

@admin.register(Innovation)
class InnovationAdmin(admin.ModelAdmin):
    list_display = ('title', 'innovation_type', 'developed_by', 'is_featured', 'created_at')
    list_filter = ('innovation_type', 'is_featured')
    search_fields = ('title', 'description', 'developed_by')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured',)
