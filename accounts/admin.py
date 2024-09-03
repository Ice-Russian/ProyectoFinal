from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'profile_image', 'biography')
    search_fields = ('user__username', 'first_name', 'last_name', 'email')
    list_filter = ('user__is_active', 'user__is_staff', 'user__is_superuser')

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'profile_image', 'biography')}),
    )
