from django.contrib import admin
from .models import Post
from unfold.admin import ModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title','created_at', 'category', 'created_by')
    search_fields = ['title', 'created_by__username',]
    ordering = ('-created_at',)