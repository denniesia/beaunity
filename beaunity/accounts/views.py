from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, login
from .forms import AppUserCreationForm
from django.urls import reverse_lazy
# Create your views here.

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response