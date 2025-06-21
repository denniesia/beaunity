from django.db import models
from slugify import slugify
from beaunity.common.mixins import LastUpdatedMixin, CreatedAtMixin, CreatedByMixin

from cloudinary.models import CloudinaryField
# Create your models here.
class Category(LastUpdatedMixin, CreatedAtMixin, CreatedByMixin):
    title = models.CharField(max_length=30, unique=True)
    image = CloudinaryField(blank=True, null=True, default='',)
    description = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title