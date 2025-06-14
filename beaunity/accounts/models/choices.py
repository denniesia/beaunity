from django.db import models

class SkinTypeChoices(models.TextChoices):
    NORMAL_SKIN = 'Normal Skin', 'Normal Skin'
    DRY_SKIN = 'Dry Skin', 'Dry Skin'
    OILY_SKIN = 'Oily Skin', 'Oily Skin'
    COMBINATION_SKIN = 'Combination Skin', 'Combination Skin'
    COMBINATION_SKIN_OILY = 'Combination Skin Oily', 'Combination Skin Oily'
    COMBINATION_SKIN_DRY = 'Combination Skin Dry', 'Combination Skin Dry'
    SENSITIVE_SKIN = 'Sensitive Skin', 'Sensitive Skin'