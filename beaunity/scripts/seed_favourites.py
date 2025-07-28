import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beaunity.settings")
django.setup()

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from beaunity.challenge.models import Challenge
from beaunity.event.models import Event
from beaunity.post.models import Post
from beaunity.interaction.models import Favourite


UserModel = get_user_model()


# Generating favourites for challenges
Favourite.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=1,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=2,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=3,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=1,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=2,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=3,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=3),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=1,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=4,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=2,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=5,
)

# Generating favourites for events
Favourite.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=1,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=2,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=3,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=1,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=2,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=3,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=3),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=1,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=4,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=2,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=5,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=5),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=1,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=5),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=2,
)

# Generating favourites for posts

Favourite.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=1,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=2,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=3,
)

Favourite.objects.create(
    user=UserModel.objects.get(pk=3),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=3,
)

print("🎉 All favourites seeded successfully.")
