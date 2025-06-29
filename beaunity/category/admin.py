from django.contrib import admin
from .models import Category
from unfold.admin import ModelAdmin
# Register your models here.
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('title', 'description','created_by', 'last_updated')
    ordering = ('-created_at',)
    search_fields = ('title','created_by')