from django.db import models
from beaunity.category.models import Category
from beaunity.common.mixins import CreatedByMixin, CreatedAtMixin, LastUpdatedMixin
# Create your models here.
class Post(CreatedByMixin, CreatedAtMixin, LastUpdatedMixin):
    banner = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    is_approved = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_approve_post", "Can approve posts"),
        ]

    def __str__(self):
        return self.title