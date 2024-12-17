from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
User = get_user_model()

class UserAdmin(BaseUserAdmin):

    list_display = ['username', 'email', 'is_staff']

admin.site.register(User, UserAdmin)