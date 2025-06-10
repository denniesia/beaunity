from django.db import models
from beaunity.common.mixins import LastUpdatedMixin, CreatedAtMixin, CreatedByMixin
# Create your models here.
class Category(LastUpdatedMixin, CreatedAtMixin, CreatedByMixin):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title