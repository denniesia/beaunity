from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = (
        "content",
        "content_object",
        "user",
    )
    search_fields = (
        "content",
        "user",
    )
    ordering = ("user",)
