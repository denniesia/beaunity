from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, View
from django.contrib.auth import get_user_model, login
from .forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm, AppUserEditForm
from django.urls import reverse_lazy
from django.contrib.auth.views import  LoginView
from .models import Profile
from beaunity.interaction.models import Favourite
from beaunity.event.models import Event
from beaunity.post.models import Post
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    #uses signal to create Profile
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('landing_page')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response

class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AppUserLoginForm


#Profile Views

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile-details.html'
    model = Profile
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_content_type = ContentType.objects.get_for_model(Event)
        fav_events = Event.objects.filter(
            id__in=Favourite.objects.filter(
                user=self.request.user,
                content_type=event_content_type,
            ).values_list('object_id', flat=True)
        )
        post_event_type = ContentType.objects.get_for_model(Post)
        fav_posts = Post.objects.filter(
            id__in=Favourite.objects.filter(
                user=self.request.user,
                content_type=post_event_type,
            ).values_list('object_id', flat=True)
        )
        context['fav_events'] = fav_events
        context['fav_posts'] = fav_posts
        context['my_posts'] = Post.objects.filter(created_by=self.request.user).order_by('-created_at')
        return context

class ProfileEditView(LoginRequiredMixin, View):   #LoginRequiredMixin, UserPassesTestMixin
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
        else:
            print(user_form.errors, profile_form.errors)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)
    
