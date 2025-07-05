from django.db import models
from django.contrib.auth import get_user_model


from .choices import DifficultyLevel
from beaunity.common.models import BaseActivity
from beaunity.common.mixins import LastUpdatedMixin, CreatedAtMixin, CreatedByMixin
from beaunity.category.models import Category


# Create your models here.

UserModel = get_user_model()

class Challenge(BaseActivity,LastUpdatedMixin, CreatedAtMixin, CreatedByMixin):
    progress = models.PositiveIntegerField()
    difficulty = models.CharField(
        max_length=15,
        choices=DifficultyLevel.choices,
    )
    categories = models.ManyToManyField(Category, related_name='challenge_categories')
    participants = models.ManyToManyField(UserModel, related_name='challenge_participants', blank=True)

    class Meta:
        verbose_name_plural = 'Challenges'
        permissions = (
            ("can_approve_challenge", "Can approve challenge"),
        )

    def __str__(self):
        return self.title
