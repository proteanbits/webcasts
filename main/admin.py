from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission

from main.models import UserProfile

# Register your models here.
admin.site.register(Permission)
admin.site.unregister(get_user_model())


class UserProfileInline(admin.StackedInline):
    """Create a Inline for UserProfile for Admin"""
    model = UserProfile
    fields = ('dob',)


class UserAdmin(BaseUserAdmin):
    inlines = [
        UserProfileInline,
    ]


# Now register the new UserAdmin...
admin.site.register(get_user_model(), UserAdmin)
