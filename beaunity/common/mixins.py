from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


UserModel = get_user_model()

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