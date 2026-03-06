from django.contrib import admin
from .models import NewsUpdate, CoreValue, ValueExample

class ValueExampleInline(admin.TabularInline):
    model = ValueExample
    extra = 1

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    inlines = [ValueExampleInline]

@admin.register(NewsUpdate)
class NewsUpdateAdmin(admin.ModelAdmin):
    list_display = ('text', 'icon_type', 'is_active', 'order')
    list_filter = ('is_active', 'icon_type')
    list_editable = ('is_active', 'order')
