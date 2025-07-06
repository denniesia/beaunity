from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,  DetailView, UpdateView, DeleteView
from beaunity.common.utils.mixins import FilteredQuerysetMixin, FilteredContextMixin
from .models import Challenge
from .forms import  ChallengeCreateForm

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

class ChallengeCreateView(LoginRequiredMixin, CreateView):
    model = Challenge
    template_name = 'challenge/challenge-create.html'
    form_class = ChallengeCreateForm
    success_url = reverse_lazy('challenges')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    

class ChallengeDetailsView(DetailView):
    model = Challenge
    template_name = 'challenge/challenge-details.html'
    context_object_name = 'challenge'