from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Challenge


@admin.register(Challenge)
class ChallengeAdmin(ModelAdmin):
    list_display = (
        'title',
        'created_by',
        'created_at',
        'start_time',
        'end_time'
    )
    ordering = ('-created_at',)
    search_fields = (
        'title',
        'created_by',
    )