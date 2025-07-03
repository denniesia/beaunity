from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from .forms import CommentEditForm
from django.views.generic import UpdateView, DeleteView
from beaunity.post.models import Post
from beaunity.event.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class CommentEditView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'comment/comment-edit.html'

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.content_object.pk })

@login_required(login_url='login')
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    content_object = comment.content_object

    if request.method == 'POST' and comment.created_by == request.user:
        comment.delete()

        if isinstance(content_object, Post):
            return redirect('post-details', pk=content_object.pk)
        elif isinstance(content_object, Event):
            return redirect('event-details', pk=content_object.pk)


    if isinstance(content_object, Post):
        return redirect('forum-dashboard')
    elif isinstance(content_object, Event):
        return redirect('events')

