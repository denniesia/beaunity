
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from beaunity.category.models import Category
from beaunity.comment.forms import CommentCreateForm
from beaunity.common.mixins import UserIsCreatorMixin
from beaunity.common.forms import SearchForm
from beaunity.common.views import approve_instance, disapprove_instance
from beaunity.interaction.models import Like
from beaunity.post.models import Post
from beaunity.post.forms import AdminPostEditForm, PostCreateForm, PostEditForm, PostDeleteForm


class ForumDashboardView(ListView):
    model = Post
    template_name = "post/forum-dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchForm(self.request.GET)

        categories = Category.objects.all().prefetch_related("posts")

        category_posts = []
        for category in categories:
            posts = category.posts.filter(
                is_approved=True
            ).order_by(
                "-created_at"
            )[:5]

            category_posts.append(
                (category, posts)
            )

        context["category_posts"] = category_posts
        context["form"] = form
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)

        if form.is_valid() and form.cleaned_data["query"]:
            query = form.cleaned_data["query"]

            return Post.objects.filter(
                Q(title__icontains=query)
                    |
                Q(content__icontains=query),
                is_approved=True,
            ).order_by("-created_at")

        return Post.objects.filter(
            is_approved=True
        ).order_by(
            "-created_at"
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "post/post-create.html"

    def get_success_url(self):
        if self.request.user.has_perm("post.can_post_without_approval"):
            return reverse(
                "category-details", kwargs={"category_slug": self.object.category.slug}
            )
        else:
            return reverse_lazy("post-confirmation")

    def get_initial(self):
        initial = super().get_initial()
        slug = self.request.GET.get("category")

        if slug:
            category = get_object_or_404(Category, slug=slug)
            initial["category"] = category.pk

        return initial

    def form_valid(self, form):
        post = form.save(commit=False)

        post.created_by = self.request.user

        if self.request.user.has_perm("post.can_post_without_approval"):
            post.is_approved = True

        post.save()
        return super().form_valid(form)


@login_required(login_url="login")
def post_confirmation(request):
    return render(request, "post/post-create-confirmation.html")


@method_decorator(login_required, name="post")
class PostDetailsView(DetailView):
    model = Post
    template_name = "post/post-details.html"
    context_object_name = "post"

    def get_object(self):
        post = super().get_object()

        if not post.is_approved and not self.request.user.has_perm("post.can_approve_post"):
            raise PermissionDenied("You do not have permission to view this post.")

        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentCreateForm()
        comments = self.object.comments.all().order_by("created_at")

        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user

            comment.content_type = ContentType.objects.get_for_model(self.object)
            comment.object_id = self.object.pk
            comment.save()
            return redirect(request.META.get("HTTP_REFERER") + f"#{self.object.id}")

        return redirect(reverse("post-details", kwargs={"pk": self.object.id}))


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post/post-edit.html"

    def test_func(self):
        post = self.get_object()
        user = self.request.user
        return (
            user == post.created_by and post.is_approved
            or user.has_perm('post.can_approve_posts')
        )

    def handle_no_permission(self):
        return redirect("post-details", pk=self.get_object().pk)

    def get_success_url(self):
        if self.request.user.has_perm('post.can_approve_posts') and not self.object.is_approved:
            return reverse_lazy("post-pending")
        return reverse_lazy("post-details", kwargs={"pk": self.get_object().pk})

    def get_form_class(self):
        post = self.get_object()
        user = self.request.user

        if user.has_perm('post.can_approve_posts') and not post.is_approved:
            return AdminPostEditForm

        if post.is_approved and user == post.created_by:
            return PostEditForm

        raise PermissionDenied("You are not allowed to edit this post.")

    def get_initial(self):
        return self.object.__dict__


class PostDeleteView(LoginRequiredMixin, UserIsCreatorMixin, DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = "post/post-delete.html"
    success_url = reverse_lazy("forum-dashboard")

    def get_initial(self):
        return self.object.__dict__

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class PendingPostsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    template_name = "post/pending-posts.html"
    permission_required = "post.can_approve_post"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(
            is_approved=False
        ).order_by(
            "created_at"
        )


@login_required(login_url="login")
def approve_post(request, pk):
    return approve_instance(
        request=request,
        model_class=Post,
        pk=pk,
        content_type="post",
        permission_required="post.can_approve_post",
        redirect_approved="post-pending",
        redirect_fallback="post-pending",
    )


@login_required(login_url="login")
def disapprove_post(request, pk):
    return disapprove_instance(
        request=request,
        model_class=Post,
        pk=pk,
        permission_required="post.can_approve_post",
        redirect_disapproved="post-pending",
        redirect_fallback="post-pending",
    )


