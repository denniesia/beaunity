from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Category
from .forms import CategoryCreateForm, CategoryDeleteForm, CategoryEditForm
from django.urls import reverse_lazy
from datetime import timezone
from django.db.models import Q
# Create your views here.
class CategoryOverviewView(ListView):
    template_name = 'category/category-overview.html'
    model = Category

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return self.model.objects.filter(
                Q(title__icontains=query)
                |
                Q(description__icontains=query)
            )
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context

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
        #pk=self.kwargs.get(self.pk_url_kwarg)
        #category=self.mocel.object.get(pk=pk)
        return self.object.__dict__

    #TODO: What happens if i delete def post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)

class CategoryDetailsView(DetailView):
    model = Category
    template_name = 'category/category-details.html'
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_posts = self.object.posts.filter(is_approved=True)
        context['posts'] = category_posts
        return context

