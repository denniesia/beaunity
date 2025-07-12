from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Count
from django.utils.timezone import now

UserModel = get_user_model()


class UserIsSelfMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.pk == self.get_object().pk


class UserIsCreatorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.pk == self.get_object().created_by.pk


class LastUpdatedMixin(models.Model):
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class ContentMixin(models.Model):
    content = models.TextField(
        validators=[
            MinLengthValidator(5),
        ]
    )

    class Meta:
        abstract = True


class IsApprovedMixin(models.Model):
    is_approved = models.BooleanField(default=False)

    class Meta:
        abstract = True
