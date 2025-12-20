from django.contrib import admin
from .models import ReflectionScenario, ReflectionOption, UserResponse

class ReflectionOptionInline(admin.TabularInline):
    model = ReflectionOption
    extra = 4
    fields = ['option_text']

@admin.register(ReflectionScenario)
class ReflectionScenarioAdmin(admin.ModelAdmin):
    list_display = ['title', 'related_value', 'active_date', 'response_count']
    list_filter = ['related_value', 'active_date']
    search_fields = ['title', 'scenario_text']
    date_hierarchy = 'active_date'
    inlines = [ReflectionOptionInline]
    
    fieldsets = (
        ('Scenario Details', {
            'fields': ('title', 'scenario_text', 'related_value', 'active_date')
        }),
        ('Educational Content', {
            'fields': ('explanation',),
            'classes': ('wide',)
        }),
    )
    
    def response_count(self, obj):
        return obj.responses.count()
    response_count.short_description = 'Total Responses'

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'scenario', 'selected_option', 'created_at']
    list_filter = ['scenario__related_value', 'created_at']
    search_fields = ['user__username', 'scenario__title']
    date_hierarchy = 'created_at'
    readonly_fields = ['user', 'scenario', 'selected_option', 'created_at']
    
    def user_display(self, obj):
        return obj.user.username if obj.user else 'Anonymous'
    user_display.short_description = 'User'
    
    def has_add_permission(self, request):
        return False
