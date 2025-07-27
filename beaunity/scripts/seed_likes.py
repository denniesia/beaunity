from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from beaunity.challenge.models import Challenge
from beaunity.event.models import Event
from beaunity.post.models import Post
from beaunity.interaction.models import Like


UserModel = get_user_model()


# Generating likes for challenges
Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=3,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=3,
)

Like.objects.create(
    user=UserModel.objects.get(pk=3),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=4,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Challenge),
    object_id=5,
)


# Generating likes for events
Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=3,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=3,
)

Like.objects.create(
    user=UserModel.objects.get(pk=3),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=4,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Event),
    object_id=5,
)


# Generating likes for posts
Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=1),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=3,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=2),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=3,
)

Like.objects.create(
    user=UserModel.objects.get(pk=3),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=1,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=4,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=2,
)

Like.objects.create(
    user=UserModel.objects.get(pk=4),
    content_type=ContentType.objects.get_for_model(Post),
    object_id=5,
)

