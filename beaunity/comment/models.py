from django.db import models

from beaunity.common.mixins import (ContentMixin, CreatedAtMixin,
                                    CreatedByMixin, LastUpdatedMixin)
from beaunity.common.models import InteractionBaseModel


class Comment(LastUpdatedMixin, CreatedAtMixin, ContentMixin, InteractionBaseModel):
    pass