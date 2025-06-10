from django.shortcuts import render
from django.views.generic import ListView
from .models import Category

# Create your views here.
class CategoryOverviewView(ListView):
    template_name = 'category/category-overview.html'

    def get_queryset(self):
        return Category.objects.all()


