from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, View
from django.contrib.auth import get_user_model, login
from .forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm, AppUserEditForm
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

class ProfileEditView(LoginRequiredMixin, View):   #LoginRequiredMixin, UserPassesTestMixin
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': request.user.pk})

    def get(self,request, *args, **kwargs):
        user_form = AppUserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)

    def post(self,request, *args, **kwargs):
        user_form = AppUserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST,  request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse_lazy('profile-details',kwargs={'pk': request.user.pk} ))

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)