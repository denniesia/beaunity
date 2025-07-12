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

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    #no login

class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AppUserLoginForm

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(Profile, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        user = profile.user


        event_content_type = ContentType.objects.get_for_model(Event)
        fav_events = Event.objects.filter(
            id__in=Favourite.objects.filter(
                user=user,
                content_type=event_content_type,
            ).values_list('object_id', flat=True)
        )


        post_content_type = ContentType.objects.get_for_model(Post)
        fav_posts = Post.objects.filter(
            id__in=Favourite.objects.filter(
                user=user,
                content_type=post_content_type,
            ).values_list('object_id', flat=True)
        )

        challenge_content_type=ContentType.objects.get_for_model(Challenge)
        fav_challenges = Challenge.objects.filter(
            id__in=Favourite.objects.filter(
                user=user,
                content_type=challenge_content_type,
            ).values_list('object_id', flat=True)
        )

        context.update({
            'fav_events': fav_events,
            'fav_posts': fav_posts,
            'fav_challenges': fav_challenges,
            'my_posts': Post.objects.filter(created_by=user, is_approved=True).order_by('-created_at'),
            'joined_events': Event.objects.filter(attendees=user),
            'joined_challenges': Challenge.objects.filter(attendees=user),
            'challenges': Challenge.objects.filter(created_by=user, is_approved=True).order_by('-start_time'),
            'profile_user': user,  # optional: for easy reference in template
        })
        return context



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



