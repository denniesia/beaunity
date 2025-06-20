from django.shortcuts import render, reverse
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from .forms import CommentEditForm
from django.views.generic import UpdateView


# Create your views here.

class CommentEditView(UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'comment/comment-edit.html'

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.content_object.pk })