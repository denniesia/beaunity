from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Event


# Register your models here.
@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ("title", "created_by", "created_at", "start_time", "end_time")
    search_fields = [
        "title",
        "created_by",
    ]
    ordering = ("-created_at",)
