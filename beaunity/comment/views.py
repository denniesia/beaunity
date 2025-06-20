from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from .forms import CommentCreateForm
from django.views.generic import CreateView


# Create your views here.