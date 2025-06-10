from django.db import models
from beaunity.common.mixins import LastUpdatedMixin, CreatedAtMixin, CreatedByMixin
from django.contrib.auth import get_user_model
# Create your models here.

UserModel = get_user_model()

class Category(LastUpdatedMixin, CreatedAtMixin, CreatedByMixin):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.title