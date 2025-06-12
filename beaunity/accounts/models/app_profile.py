from .app_user import AppUser
from django.contrib.auth import get_user_model
from django.db import models
from beaunity.common.mixins import LastUpdatedMixin

from cloudinary.models import CloudinaryField

UserModel = get_user_model()

class Profile(LastUpdatedMixin):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profile_pic = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='',
    )
    first_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    bio = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    skin_type = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

