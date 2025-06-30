from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from cloudinary.models import CloudinaryField

from beaunity.common.mixins import CreatedByMixin, CreatedAtMixin, LastUpdatedMixin
from beaunity.category.models import Category
from beaunity.interaction.models import Like
from beaunity.comment.models import Comment
# Create your models here.

UserModel = get_user_model()

class Event(CreatedByMixin, CreatedAtMixin, LastUpdatedMixin):
    poster_image = CloudinaryField()
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(10)
        ]
    )
    details = models.TextField(
        validators=[
            MinLengthValidator(100)
        ]
    )
    is_online = models.BooleanField()
    is_public = models.BooleanField()
    city = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2)
        ]
    )
    location = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(10)
        ]
    )
    meeting_link = models.URLField(
        blank=True,
        null=True
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    categories = models.ManyToManyField(Category, related_name='events')
    attendees = models.ManyToManyField(UserModel, related_name='events_attendees', blank=True)
    likes = GenericRelation(Like)
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name_plural = 'Events'
        permissions = [
            ("can_approve_event", "Can approve events"),
            ("can_join_event", "Can join events"),
            ("can_host_event", "Can host events"),
        ]

    def __str__(self):
        return self.title