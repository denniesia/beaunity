from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = (
        "title",
        "is_approved",
        "created_at",
        "category",
        "created_by"
    )
    ordering = ("-created_at",)
    search_fields = (
        "title",
        "created_by__username",
    )

