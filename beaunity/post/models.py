from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from beaunity.category.models import Category
from beaunity.comment.models import Comment
from beaunity.common.mixins import ContentMixin, CreatedAtMixin,  CreatedByMixin, IsApprovedMixin, LastUpdatedMixin
from beaunity.interaction.models import Favourite, Like


# Create your models here.
class Post(CreatedByMixin, CreatedAtMixin, LastUpdatedMixin, IsApprovedMixin, ContentMixin):
    banner = models.URLField(null=True, blank=True)
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5),
        ],
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )

    comments = GenericRelation(Comment)
    likes = GenericRelation(Like)
    favourites = GenericRelation(Favourite)

    class Meta:
        permissions = [
            ("can_approve_post", "Can approve posts"),
            ("can_post_without_approval", "Can post without approval"),
        ]
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("post-details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
