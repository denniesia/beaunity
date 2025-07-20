from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin

from .forms import AppUserCreationForm

UserModel = get_user_model()


@admin.register(UserModel)
class Admin(ModelAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "username",
        "email"
    )
    add_form = AppUserCreationForm

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ()}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password"),
            },
        ),
    )
