from django.contrib.auth import admin as auth_admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Register your models here


UserModel = get_user_model()

@admin.register(UserModel)
class Admin(auth_admin.UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', )
    search_fields = ('username', 'email')

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
                "fields": ("username", "password1", "password2"),
            },
        ),
    )