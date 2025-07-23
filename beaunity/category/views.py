from datetime import timezone

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import CategoryCreateForm, CategoryDeleteForm, CategoryEditForm, SearchForm
from .models import Category


class CategoryOverviewView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    template_name = "category/category-overview.html"
    model = Category
    permission_required = "category.add_category"
    context_object_name = "categories"

    def get_queryset(self):
        self.form = SearchForm(self.request.GET)
        queryset = self.model.objects.all()

        if self.form.is_valid():
            query = self.form.cleaned_data.get("query")
            if query:
                queryset = queryset.filter(
                    Q(title__icontains=query)
                        |
                    Q(description__icontains=query)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["query"] = self.request.GET.get("query", "")
        return context


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = "category/category-create.html"
    permission_required = "category.add_category"
    success_url = reverse_lazy("category-overview")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CategoryEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryEditForm
    template_name = "category/category-edit.html"
    permission_required = "category.change_category"
    slug_url_kwarg = "category_slug"
    success_url = reverse_lazy("category-overview")


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = "category/category-delete.html"
    form_class = CategoryDeleteForm
    slug_url_kwarg = "category_slug"
    permission_required = "category.delete_category"
    success_url = reverse_lazy("category-overview")

    def get_initial(self):
        return self.object.__dict__

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CategoryDetailsView(DetailView):
    model = Category
    template_name = "category/category-details.html"
    context_object_name = "category"
    slug_url_kwarg = "category_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_posts = self.object.posts.filter(is_approved=True)

        paginator = Paginator(category_posts, 6)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["posts"] = page_obj

        return context
