from django.contrib import admin
from .models import Comment
from unfold.admin import ModelAdmin
# Register your models here.

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('content', 'content_object', 'created_by', )
    search_fields = ['content','created_by',]
    ordering = ('-created_at',)