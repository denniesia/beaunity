from django.db import models
from beaunity.category.models import Category
from beaunity.common.mixins import ContentMixin, CreatedByMixin, CreatedAtMixin, LastUpdatedMixin
from django.core.validators import MinLengthValidator
from django.contrib.contenttypes.fields import GenericRelation
from beaunity.comment.models import Comment
from beaunity.interaction.models import Like, Favourite

# Create your models here.
class Post(CreatedByMixin, CreatedAtMixin, LastUpdatedMixin, ContentMixin):
    banner = models.URLField(null=True, blank=True)
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5),
        ]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    is_approved = models.BooleanField(default=False)

    comments = GenericRelation(Comment)
    likes = GenericRelation(Like)
    favourites = GenericRelation(Favourite)

    class Meta:
        permissions = [
            ("can_approve_post", "Can approve posts"),
            ('can_post_without_approval', 'Can post without approval'),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return self.title