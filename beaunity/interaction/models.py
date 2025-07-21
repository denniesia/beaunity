from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

UserModel = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        "content_type",
        "object_id")

    class Meta:
        unique_together = (
            "user",
            "content_type",
            "object_id"
        )


class Favourite(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        "content_type",
        "object_id"
    )

    class Meta:
        unique_together = (
            "user",
            "content_type",
            "object_id"
        )
