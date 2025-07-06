from django.shortcuts import render
from django.views.generic import ListView,CreateView,  DetailView, UpdateView, DeleteView
from beaunity.common.utils.mixins import FilteredQuerysetMixin, FilteredContextMixin
from .models import Challenge

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ChallengeOverviewView(LoginRequiredMixin, FilteredContextMixin, FilteredQuerysetMixin, ListView):
    model = Challenge
    ordering = ['-start_time']
    template_name = 'challenge/challenges-overview.html'
    context_object_name = 'challenges'
    paginate_by = 5

    def get_queryset(self):
        return self.get_filtered_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_filtered_context(context, self.model)