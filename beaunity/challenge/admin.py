from django.contrib import admin
from .models import Challenge
from unfold.admin import ModelAdmin
# Register your models here.
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