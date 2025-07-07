from PycharmProjects.pythonProjectDev.Advanced.functions_advanced_exc.keyword_arguments_length import kwargs_length
from beaunity.common.mixins import UserIsCreatorMixin
from django.shortcuts import render
from django.template.base import kwarg_re
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,  DetailView, UpdateView, DeleteView
from beaunity.common.utils.mixins import FilteredQuerysetMixin, FilteredContextMixin
from .models import Challenge
from .forms import  ChallengeCreateForm, ChallengeEditForm, ChallengeDeleteForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

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

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('challenge-details', kwargs={'pk': self.object.pk})

class ChallengeDetailsView(LoginRequiredMixin, DetailView):
    model = Challenge
    template_name = 'challenge/challenge-details.html'
    context_object_name = 'challenge'

class ChallengeEditView(UpdateView):
    model = Challenge
    form_class = ChallengeEditForm
    template_name = 'challenge/challenge-edit.html'

    def get_success_url(self):
        return reverse_lazy('challenge-details', kwargs={'pk': self.object.pk})

class ChallengeDeleteView(LoginRequiredMixin, UserIsCreatorMixin, DeleteView):
    model = Challenge
    form_class = ChallengeDeleteForm
    template_name = 'challenge/challenge-delete.html'
    success_url = reverse_lazy('challenges')

    def get_initial(self):
        return self.object.__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
            })
        return kwargs

class PendingChallengeView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Challenge
    template_name = 'challenge/pending-challenges.html'
    permission_required = 'challenge.can_approve_challenge'

    def get_queryset(self):
        return Challenge.objects.filter(is_approved=False).order_by('-created_at')

