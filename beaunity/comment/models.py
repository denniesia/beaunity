from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from beaunity.common.mixins import (ContentMixin, CreatedAtMixin,
                                    CreatedByMixin, LastUpdatedMixin)


class Comment(LastUpdatedMixin, CreatedAtMixin, CreatedByMixin, ContentMixin):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        "content_type",
        "object_id")