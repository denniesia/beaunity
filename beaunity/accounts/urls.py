from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),


]
