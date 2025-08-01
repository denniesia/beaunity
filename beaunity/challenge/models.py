from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone
from django.urls import reverse

from beaunity.category.models import Category
from beaunity.comment.models import Comment
from beaunity.common.mixins import (CreatedAtMixin, CreatedByMixin,
                                    IsApprovedMixin, LastUpdatedMixin)
from beaunity.common.models import BaseActivity
from beaunity.interaction.models import Like, Favourite

from .choices import DifficultyLevel

UserModel = get_user_model()


class Challenge(BaseActivity, LastUpdatedMixin, CreatedAtMixin, CreatedByMixin, IsApprovedMixin):
    difficulty = models.CharField(
        max_length=15,
        choices=DifficultyLevel,
        default=DifficultyLevel.BEGINNER,
    )
    categories = models.ManyToManyField(
        Category,
        related_name="challenge_categories"
    )
    attendees = models.ManyToManyField(
        UserModel,
        related_name="challenge_attendees",
        blank=True,
        null=True,
    )
    likes = GenericRelation(Like)
    comments = GenericRelation(Comment)
    favourites = GenericRelation(Favourite)

    class Meta:
        verbose_name_plural = "Challenges"
        permissions = (
            ("can_approve_challenge", "Can approve challenge"),
        )

    @property
    def model_name(self):
        return "challenge"

    @property
    def progress(self):
        now = timezone.now()

        if now <= self.start_time:
            return 0
        elif now > self.end_time:
            return 100

        total_duration = (self.end_time - self.start_time).total_seconds()
        elapsed = (now - self.start_time).total_seconds()
        return int((elapsed / total_duration) * 100)

    @property
    def duration_in_weeks(self):
        duration = self.end_time - self.start_time
        return (duration.days + 6) // 7


    def get_absolute_url(self):
        return reverse("challenge-details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
