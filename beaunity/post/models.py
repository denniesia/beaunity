from django.db import models
from beaunity.category.models import Category
from beaunity.common.mixins import CreatedByMixin, CreatedAtMixin, LastUpdatedMixin
from django.core.validators import MinLengthValidator
# Create your models here.
class Post(CreatedByMixin, CreatedAtMixin, LastUpdatedMixin):
    banner = models.URLField(null=True, blank=True)
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5),
        ]
    )
    content = models.TextField(
        validators=[
            MinLengthValidator(5),
        ]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    is_approved = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_approve_post", "Can approve posts"),
        ]

    def __str__(self):
        return self.title