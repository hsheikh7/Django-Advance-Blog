from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User 

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = = ("email", "is_superuser", "is_active", "is_verified")
    list_filter = = ("email", "is_superuser", "is_active", "is_verified")
    searching_fields = ("email",)
    ordering = ("email",)

admin.site.register(User, CustomUserAdmin)
