from django.contrib import admin
from .models import Category
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','created_by', 'last_updated')
    ordering = ('-last_updated',)
    search_fields = ('title','created_by')