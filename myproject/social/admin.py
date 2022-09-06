from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as ua

from .models import Profile, Messages

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(ua):
    model = User
    # Change fields displayed in Admin console overview
    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("username", "email", "is_staff", "is_active")
    # Group Fields together
    fieldsets = (
        (None, {"fields": ("username", "password", "first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email", "is_staff", "is_active", "is_superuser")
        })
    )
    # Add Profile under User
    inlines = [ProfileInline]
    # Add search bar and include below fields to be searched
    search_fields = ("username", "first_name", "last_name", "email")
    

class MessageAdmin(admin.ModelAdmin):
    model = Messages
    # Change fields displayed in Admin console overview
    list_display = ("user", "body", "created_at")
    list_filter = ("user", "created_at")
    # Add search bar and include below fields to be searched
    search_fields = ["user"]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Messages, MessageAdmin)