from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_at', 'category', 'created_by')
    search_fields = ['title', 'created_by',]
    ordering = ('-created_at',)