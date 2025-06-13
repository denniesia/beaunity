from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from beaunity.category.models import Category
from django.urls import reverse_lazy
from .forms import PostEditForm
from beaunity.post.models import Post

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


class PostDetailsView(DetailView):
    model = Post
    template_name = 'post/post-details.html'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post/post-edit.html'

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    pass