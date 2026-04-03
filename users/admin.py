
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.action(description='Block selected users')
def block_users(modeladmin, request, queryset):
    queryset.update(is_blocked=True)

@admin.action(description='Unblock selected users')
def unblock_users(modeladmin, request, queryset):
    queryset.update(is_blocked=False)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_blocked', 'is_active', 'date_joined']
    list_filter = ['is_blocked', 'is_active', 'is_staff', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    actions = [block_users, unblock_users]
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('profile_picture', 'contact_number', 'is_blocked')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
