from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Favourite, Like


@admin.register(Like)
class LikeAdmin(ModelAdmin):
    list_display = (
        "user",
        "content_object",
        "object_id",
        "content_type",
    )
    search_fields = ("user",)


@admin.register(Favourite)
class FavouriteAdmin(ModelAdmin):
    list_display = (
        "user",
        "content_object",
        "object_id",
        "content_type",
    )
    search_fields = ("user",)
