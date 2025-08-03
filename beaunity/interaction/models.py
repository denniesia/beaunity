from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from beaunity.common.models import InteractionBaseModel


UserModel = get_user_model()

class Like(InteractionBaseModel):
    pass


class Favourite(InteractionBaseModel):
    pass