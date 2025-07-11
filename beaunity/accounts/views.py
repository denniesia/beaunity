from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth import get_user_model, login, logout
from .forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm, AppUserEditForm
from django.urls import reverse_lazy
from django.contrib.auth.views import  LoginView
from .models import Profile
from beaunity.interaction.models import Favourite
from beaunity.event.models import Event
from beaunity.post.models import Post
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from beaunity.common.mixins import UserIsSelfMixin
from beaunity.challenge.models import Challenge
# Create your views here.

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    #uses signal to create Profile
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('landing-page')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    #no login

class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AppUserLoginForm

class ProfileDetailView(LoginRequiredMixin,UserIsSelfMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'

class ProfileEditView(LoginRequiredMixin, UserIsSelfMixin, UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit.html'

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

class ProfileDeleteView(LoginRequiredMixin,UserIsSelfMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('landing-page')

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.is_active = False
        profile.save()
        logout(request)
        return redirect(self.success_url)



