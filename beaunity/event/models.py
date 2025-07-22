from datetime import datetime

from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from beaunity.category.models import Category
from beaunity.comment.models import Comment
from beaunity.common.mixins import CreatedAtMixin, CreatedByMixin, LastUpdatedMixin
from beaunity.common.models import BaseActivity
from beaunity.interaction.models import Like

UserModel = get_user_model()


class Event(BaseActivity, LastUpdatedMixin, CreatedAtMixin, CreatedByMixin):
    is_public = models.BooleanField(default=True)
    categories = models.ManyToManyField(
        Category,
        related_name="events"
    )
    attendees = models.ManyToManyField(
        UserModel,
        related_name="event_attendees",
        blank=True
    )
    likes = GenericRelation(Like)
    comments = GenericRelation(Comment)

    @property
    def model_name(self):
        return "event"

    class Meta:
        verbose_name_plural = "Events"

    def get_absolute_url(self):
        return reverse("event-details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
