from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from .validators import OnlyDigitsValidator, FourUniqueDigitsValidator
# Create your models here.
class Organizer(models.Model):
    company_name = models.CharField(
        max_length=110,
        unique=True,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                '^[a-zA-Z0-9\s-]+$',
                "The company name is invalid!" ,
                code='invalid_company_name')
        ]
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            OnlyDigitsValidator()
        ]
    )
    secret_key = models.CharField(
        max_length=4,
        validators=[
            FourUniqueDigitsValidator()
        ]
    )
    website = models.URLField(
        null=True,
        blank=True,
    )