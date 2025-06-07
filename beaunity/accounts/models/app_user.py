from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from beaunity.accounts.managers import AppUserManager

from django.contrib.auth.models import AbstractUser

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    username = models.CharField(
        max_length=30,
        unique=True,
        error_messages={
            'unique': 'A user with that username already exists.'
        },

    )
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AppUserManager()
