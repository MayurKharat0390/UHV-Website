from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_student', 'is_faculty', 'is_staff', 'date_joined']
    list_filter = ['is_student', 'is_faculty', 'is_staff', 'is_superuser', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    fieldsets = UserAdmin.fieldsets + (
        ('UHV Roles', {'fields': ('is_student', 'is_faculty')}),
    )
    
    actions = ['make_student', 'make_faculty']
    
    def make_student(self, request, queryset):
        queryset.update(is_student=True, is_faculty=False)
        self.message_user(request, f"{queryset.count()} users marked as students.")
    make_student.short_description = "Mark selected users as Students"
    
    def make_faculty(self, request, queryset):
        queryset.update(is_student=False, is_faculty=True)
        self.message_user(request, f"{queryset.count()} users marked as faculty.")
    make_faculty.short_description = "Mark selected users as Faculty"
