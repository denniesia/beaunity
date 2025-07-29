from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy

from beaunity.common.mixins import UserIsCreatorMixin

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
