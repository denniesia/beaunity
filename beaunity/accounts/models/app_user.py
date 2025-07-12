from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from beaunity.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True, error_messages={"unique": "A user with that email already exists."}
    )
    username = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
        error_messages={"unique": "A user with that username already exists."},
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = AppUserManager()
