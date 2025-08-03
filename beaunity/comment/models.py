from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from beaunity.common.mixins import (ContentMixin, CreatedAtMixin,
                                    CreatedByMixin, LastUpdatedMixin)
from beaunity.common.models import InteractionBaseModel


class Comment(LastUpdatedMixin, CreatedAtMixin, ContentMixin, InteractionBaseModel):
    pass