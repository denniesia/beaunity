from django.shortcuts import render
from django.views.generic import ListView,CreateView,  DetailView, UpdateView, DeleteView

from .models import Challenge
# Create your views here.
class ChallengeOverviewView(ListView):
    model = Challenge
    ordering = ['-start_time']
    template_name = 'challenge/challenge-overview.html'
