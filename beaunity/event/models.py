from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from beaunity.common.mixins import CreatedByMixin, CreatedAtMixin, LastUpdatedMixin
from beaunity.category.models import Category
from beaunity.interaction.models import Like
from beaunity.comment.models import Comment
from beaunity.common.models import BaseActivity
from ckeditor.fields import RichTextField
# Create your models here.

UserModel = get_user_model()

class Event(BaseActivity, CreatedByMixin, CreatedAtMixin, LastUpdatedMixin):
    is_public = models.BooleanField()
    categories = models.ManyToManyField(Category, related_name='events')
    attendees = models.ManyToManyField(UserModel, related_name='events_attendees', blank=True)
    likes = GenericRelation(Like)
    comments = GenericRelation(Comment)

    @property
    def model_name(self):
        return "event"

    class Meta:
        verbose_name_plural = 'Events'
        permissions = [
            ("can_join_event", "Can join events"),
        ]

    def __str__(self):
        return self.title


