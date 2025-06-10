from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Category
from .forms import CategoryCreateForm
# Create your views here.
class CategoryOverviewView(ListView):
    template_name = 'category/category-overview.html'

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'category/category-create.html'