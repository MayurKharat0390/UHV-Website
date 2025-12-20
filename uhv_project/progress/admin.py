from django.contrib import admin
from .models import UserProgress, ReflectionStreak, LoginStreak
from django.utils.html import format_html

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_logins', 'total_reflections', 'current_streak_display', 'longest_streak_display', 'total_journal_entries', 'last_login_date']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at', 'streak_chart']
    list_filter = ['last_login_date']
    
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Login Stats', {
            'fields': ('total_logins', 'last_login_date')
        }),
        ('Reflection Stats', {
            'fields': ('total_reflections', 'current_streak', 'longest_streak', 'last_reflection_date')
        }),
        ('Journal Stats', {
            'fields': ('total_journal_entries',)
        }),
        ('Streak Visualization', {
            'fields': ('streak_chart',),
            'classes': ('wide',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def current_streak_display(self, obj):
        if obj.current_streak >= 7:
            return format_html('<strong style="color: green;">🔥 {} days</strong>', obj.current_streak)
        elif obj.current_streak >= 3:
            return format_html('<span style="color: orange;">🔥 {} days</span>', obj.current_streak)
        else:
            return f'{obj.current_streak} days'
    current_streak_display.short_description = 'Current Streak'
    
    def longest_streak_display(self, obj):
        return format_html('<strong>🏆 {} days</strong>', obj.longest_streak)
    longest_streak_display.short_description = 'Best Streak'
    
    def streak_chart(self, obj):
        streaks = LoginStreak.objects.filter(user=obj.user).order_by('-date')[:30]
        chart_html = '<div style="display: flex; gap: 2px; flex-wrap: wrap;">'
        for streak in reversed(list(streaks)):
            color = '#10b981'  # Green for any login
            chart_html += f'<div style="width: 20px; height: 20px; background: {color}; border-radius: 4px;" title="{streak.date} - {streak.login_count} logins"></div>'
        chart_html += '</div><p style="margin-top: 10px; color: #666;">Last 30 days (Green = Logged in)</p>'
        return format_html(chart_html)
    streak_chart.short_description = 'Login Activity Chart'

@admin.register(LoginStreak)
class LoginStreakAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'login_count', 'login_display']
    list_filter = ['date']
    search_fields = ['user__username']
    date_hierarchy = 'date'
    readonly_fields = ['login_count']
    
    def login_display(self, obj):
        return format_html('<span style="color: green;">✓ {} logins</span>', obj.login_count)
    login_display.short_description = 'Status'

@admin.register(ReflectionStreak)
class ReflectionStreakAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'reflection_completed_display']
    list_filter = ['reflection_completed', 'date']
    search_fields = ['user__username']
    date_hierarchy = 'date'
    
    def reflection_completed_display(self, obj):
        if obj.reflection_completed:
            return format_html('<span style="color: green;">✓ Completed</span>')
        return format_html('<span style="color: gray;">○ Not completed</span>')
    reflection_completed_display.short_description = 'Status'
    
    actions = ['mark_completed', 'mark_incomplete']
    
    def mark_completed(self, request, queryset):
        queryset.update(reflection_completed=True)
        self.message_user(request, f"{queryset.count()} days marked as completed.")
    mark_completed.short_description = "Mark as completed"
    
    def mark_incomplete(self, request, queryset):
        queryset.update(reflection_completed=False)
        self.message_user(request, f"{queryset.count()} days marked as incomplete.")
    mark_incomplete.short_description = "Mark as incomplete"
