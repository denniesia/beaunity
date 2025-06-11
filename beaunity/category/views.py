from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Category
from .forms import CategoryCreateForm, CategoryDeleteForm, CategoryEditForm
from django.urls import reverse_lazy
from datetime import timezone
# Create your views here.
class CategoryOverviewView(ListView):
    template_name = 'category/category-overview.html'

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'category/category-create.html'
    success_url = reverse_lazy('category-overview')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CategoryEditView(UpdateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'category/category-edit.html'
    slug_url_kwarg = 'category_slug'

    def get_success_url(self):
        return reverse_lazy('category-overview')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category-delete.html'
    form_class = CategoryDeleteForm
    slug_field = 'slug'
    slug_url_kwarg = 'category_slug'

    success_url = reverse_lazy('category-overview')

    def get_initial(self):
        return self.object.__dict__

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)