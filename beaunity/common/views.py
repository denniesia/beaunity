from django.shortcuts import render
from django.views.generic import ListView
from beaunity.category.models import Category
# Create your views here.
class IndexView(ListView):
    template_name = 'common/landing_page.html'

    def get_queryset(self):
        return Category.objects.all()