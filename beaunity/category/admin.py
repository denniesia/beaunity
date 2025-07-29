from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "title",
        "description",
        "created_by",
        "last_updated")
    ordering = (
        "-created_at",
    )
    search_fields = (
        "title",
        "created_by"
    )
