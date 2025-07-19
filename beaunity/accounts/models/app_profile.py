from .app_user import AppUser
from django.contrib.auth import get_user_model
from django.db import models
from beaunity.common.mixins import LastUpdatedMixin
from beaunity.event.models import Event
from beaunity.challenge.models import Challenge
from .choices import SkinTypeChoices
from datetime import date
from cloudinary.models import CloudinaryField

UserModel = get_user_model()


class Profile(LastUpdatedMixin):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profile_pic = CloudinaryField(
        "image",
        blank=True,
        null=True,
        default="",
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
        max_length=30,
        null=True,
        blank=True,
        choices=SkinTypeChoices,
    )

    @property
    def age(self):
        if not self.date_of_birth:
            return None

        today = date.today()
        return (today.year - self.date_of_birth.year -
                ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)))


    @property
    def full_name(self):
        first = self.first_name.title() if self.first_name else ""
        last = self.last_name.title() if self.last_name else ""
        return f"{first} {last}".strip()
