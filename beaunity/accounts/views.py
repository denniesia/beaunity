from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  UpdateView, View)

from beaunity.challenge.models import Challenge
from beaunity.common.mixins import UserIsSelfMixin
from beaunity.event.models import Event
from beaunity.interaction.models import Favourite
from beaunity.post.models import Post

from .decorators import superuser_required
from .forms import (AppUserCreationForm, AppUserEditForm, AppUserLoginForm,
                    ProfileEditForm)
from .models import Profile


UserModel = get_user_model()


class AppUserRegisterView(UserPassesTestMixin,CreateView):
    # uses signal to create Profile
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("landing-page")
    # to not throw error 403

    # no login


class AppUserLoginView(UserPassesTestMixin, LoginView):
    template_name = "accounts/login.html"
    form_class = AppUserLoginForm

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("landing-page")
    # to not throw error 403


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "accounts/profile-details.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        group = None

        if profile.user.groups.filter(name="Superuser").exists():
            group = "Superuser"
        elif profile.user.groups.filter(name="Moderator").exists():
            group = "Moderator"
        elif profile.user.groups.filter(name="Organizer").exists():
            group = "Organizer"
        elif profile.user.groups.filter(name="User").exists():
            group = "User"

        context["group"] = group
        return context


class ProfileEditView(LoginRequiredMixin, UserIsSelfMixin, UpdateView):
    model = UserModel
    template_name = "accounts/profile-edit.html"

    def get_success_url(self):
        return reverse_lazy("profile-details", kwargs={"pk": self.request.user.pk})

    def get(self, request, *args, **kwargs):
        user_form = AppUserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            "user_form": user_form,
            "profile_form": profile_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = AppUserEditForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileEditForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(
                reverse_lazy("profile-details", kwargs={"pk": request.user.pk})
            )

        context = {
            "user_form": user_form,
            "profile_form": profile_form,
        }
        return render(request, self.template_name, context)


class ProfileDeleteView(LoginRequiredMixin, UserIsSelfMixin, DeleteView):
    model = UserModel
    template_name = "accounts/profile-delete.html"
    success_url = reverse_lazy("landing-page")

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.is_active = False
        profile.save()
        logout(request)
        return redirect(self.success_url)


@superuser_required
def make_superuser(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user
    group = Group.objects.get(name="Superuser")
    group = Group.objects.get(name="Moderator")
    group = Group.objects.get(name="Organizer")
    user.is_superuser = True
    user.is_staff = True
    user.save()
    user.groups.add(group)
    return redirect("profile-details", pk)


@superuser_required
def make_moderator(request, pk):
    """
    A moderator cannot be an organizer.
    """
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user

    if user.groups.filter(name="Organizer").exists():
        user.groups.remove(Group.objects.get(name="Organizer"))
    elif user.groups.filter(name="Superuser").exists():
        user.groups.remove(Group.objects.get(name="Superuser"))

    group = Group.objects.get(name="Moderator")
    user.groups.add(group)
    user.is_staff = True
    user.save()
    return redirect("profile-details", pk=pk)


@superuser_required
def make_organizer(request, pk):
    """'
    A organizer cannot be a moderator.
    """
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user

    if user.groups.filter(name="Moderator").exists():
        user.groups.remove(Group.objects.get(name="Moderator"))
    elif user.groups.filter(name="Superuser").exists():
        user.groups.remove(Group.objects.get(name="Superuser"))

    group = Group.objects.get(name="Organizer")
    user.groups.add(group)
    user.is_staff = True
    user.save()
    return redirect("profile-details", pk=pk)


@superuser_required
def remove_roles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user

    user.groups.clear()

    group = Group.objects.get(name="User")
    user.groups.add(group)
    user.is_staff = False
    user.save()
    return redirect("profile-details", pk=pk)
