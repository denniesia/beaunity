from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

from django.core.validators import MinLengthValidator

from ckeditor.fields import RichTextField


UserModel = get_user_model()


class BaseActivity(models.Model):
    poster_image = CloudinaryField()
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(10)
        ]
    )
    details = RichTextField()
    is_online = models.BooleanField(default=False)
    meeting_link = models.URLField(
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(2)
        ]
    )
    location = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(10)
        ]
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_new = models.BooleanField(default=False)

    class Meta:
        abstract = True
