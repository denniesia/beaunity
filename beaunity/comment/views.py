from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import DeleteView, UpdateView

from beaunity.challenge.models import Challenge
from beaunity.common.mixins import UserIsCreatorMixin
from beaunity.event.models import Event
from beaunity.post.models import Post

from .forms import CommentEditForm
from .models import Comment

# Create your views here.


class CommentEditView(LoginRequiredMixin, UserIsCreatorMixin, UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = "comment/comment-edit.html"

    def get_success_url(self):
        return reverse("post-details", kwargs={"pk": self.object.content_object.pk})


@login_required(login_url="login")
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    content_object = comment.content_object

    if request.method == "POST" and comment.created_by == request.user:
        comment.delete()

        if isinstance(content_object, Post):
            return redirect("post-details", pk=content_object.pk)
        elif isinstance(content_object, Event):
            return redirect("event-details", pk=content_object.pk)
        elif isinstance(content_object, Challenge):
            return redirect("challenge-details", pk=content_object.pk)

    if isinstance(content_object, Post):
        return redirect("forum-dashboard")
    elif isinstance(content_object, Event):
        return redirect("events")
    elif isinstance(content_object, Challenge):
        return redirect("challenges")
