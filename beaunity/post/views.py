from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from beaunity.category.models import Category
from django.urls import reverse_lazy, reverse
from .forms import PostCreateForm, PostEditForm
from beaunity.comment.forms import CommentCreateForm
from beaunity.post.models import Post

from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from beaunity.common.utils import user_is_admin_or_moderator

# Create your views here.
class ForumDashboardView(TemplateView):
    template_name = 'post/forum-dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all().prefetch_related('posts')

        category_posts = []
        for category in categories:
            posts = category.posts.filter(is_approved=True).order_by('-created_at')[:5]
            category_posts.append((category, posts))

        context['category_posts'] = category_posts
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/post-create.html'

    def get_success_url(self):
        if user_is_admin_or_moderator(self.request.user):
            return reverse('category-details', kwargs={'category_slug': self.object.category.slug})
        else:
            return reverse_lazy('post-confirmation')

    def get_initial(self):
        initial = super().get_initial()
        slug = self.request.GET.get('category')
        if slug:
            category = get_object_or_404(Category, slug=slug)
            initial['category'] = category.pk

        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if self.initial.get('category'):
            form.fields['category'].widget = forms.HiddenInput()
        return form
    
    def form_valid(self, form):
        post = form.save(commit=False)
        
        post.created_by = self.request.user

        if user_is_admin_or_moderator(self.request.user):
            post.is_approved = True

        post.save()
        return super().form_valid(form)

@login_required(login_url='login')
def post_confirmation(request):
    return render(request, 'post/post-create-confirmation.html')
class PostDetailsView(DetailView):
    model = Post
    template_name = 'post/post-details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreateForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user

            comment.content_type = ContentType.objects.get_for_model(self.object)
            comment.object_id = self.object.pk
            comment.save()
            return redirect('post-details', pk = self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)



class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post/post-edit.html'

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'post/post-delete.html'
    model = Post
    success_url = reverse_lazy('forum-dashboard')



class PendingPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/pending-posts.html'

    def get_queryset(self):
        posts = Post.objects.filter(is_approved=False).order_by('-created_at')
        return posts


def forum_search(request):
    query = request.GET.get('query')

    categories = Category.objects.filter(
        Q(title__icontains=query)
            |
        Q(description__icontains=query)
    ) if query else []
    posts = Post.objects.filter(
        Q(title__icontains=query)
            |
        Q(content__icontains=query)
    ) if query else []

    context = {
        'query': query,
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'post/post-search.html', context)