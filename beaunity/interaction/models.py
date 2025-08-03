from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

UserModel = get_user_model()

class InteractionBaseModel(models.Model):
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
        abstract = True
        unique_together = (
            "user",
            "content_type",
            "object_id"
        )


class Like(InteractionBaseModel):
    pass


class Favourite(InteractionBaseModel):
    pass