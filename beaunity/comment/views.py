from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy

from beaunity.challenge.models import Challenge
from beaunity.common.mixins import UserIsCreatorMixin
from beaunity.event.models import Event
from beaunity.post.models import Post

from .forms import CommentEditForm
from .models import Comment


class CommentEditView(LoginRequiredMixin, UserIsCreatorMixin, UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = "comment/comment-edit.html"

    def get_success_url(self):
        content_object = self.object.content_object
        return content_object.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, UserIsCreatorMixin, DeleteView):
    model = Comment
    template_name = "comment/comment_confirm_delete.html"

    def get_success_url(self):
        return self.object.content_object.get_absolute_url()
