from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import get_user_model, login
from .forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from django.urls import reverse_lazy
from django.contrib.auth.views import  LoginView
from .models import Profile

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response

class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'
    form_class = AppUserLoginForm


#Profile Views

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = Profile
    context_object_name = 'profile'

class ProfileEditView(LoginRequiredMixin, UpdateView):   #LoginRequiredMixin, UserPassesTestMixin
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})