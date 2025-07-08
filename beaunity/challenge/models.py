from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from .choices import DifficultyLevel
from beaunity.common.models import BaseActivity
from beaunity.common.mixins import LastUpdatedMixin, CreatedAtMixin, CreatedByMixin, IsApprovedMixin
from beaunity.category.models import Category


# Create your models here.

UserModel = get_user_model()

class Challenge(BaseActivity, LastUpdatedMixin, CreatedAtMixin, CreatedByMixin, IsApprovedMixin):
    difficulty = models.CharField(
        max_length=15,
        choices=DifficultyLevel,
        default=DifficultyLevel.BEGINNER,
    )
    categories = models.ManyToManyField(Category, related_name='challenge_categories')
    attendees = models.ManyToManyField(UserModel, related_name='challenge_attendees', blank=True)

    class Meta:
        verbose_name_plural = 'Challenges'
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
        if self.start_time and self.end_time:
            delta = self.end_time - self.start_time
            return (delta.days + 6) // 7
        return 0

    def __str__(self):
        return self.title
