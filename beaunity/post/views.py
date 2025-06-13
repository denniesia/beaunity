from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from beaunity.category.models import Category
from django.urls import reverse_lazy

# Create your views here.
class ForumDashboardView(TemplateView):
    template_name = 'post/forum-dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all().prefetch_related('posts')

        category_posts = []
        for category in categories:
            posts = category.posts.all().order_by('-created_at')
            category_posts.append((category, posts))

        context['category_posts'] = category_posts
        return context


