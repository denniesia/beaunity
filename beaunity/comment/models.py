from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from beaunity.common.mixins import (ContentMixin, CreatedAtMixin,
                                    CreatedByMixin, LastUpdatedMixin)


# Create your models here.
class Comment(ContentMixin, CreatedByMixin, CreatedAtMixin, LastUpdatedMixin):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")