from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from accounts.models import User, Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('city', 'country')}),
        ('Geographical info', {
            'fields': (
                'latitude',
                'longitude'
            )
        }),
    )

    list_display = (
        'city',
        'country',
        'latitude',
        'longitude'
    )

    search_fields = (
        'city',
        'country'
    )


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'fullname',
                'email',
                'phone_number'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username',
        'email',
        'fullname',
        'phone_number',
        'level',
        'is_gardener',
        'is_staff'
    )

    search_fields = (
        'username',
        'fullname',
        'is_gardener',
        'phone_number',
        'email'
    )
