import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beaunity.settings")
django.setup()

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from beaunity.challenge.models import Challenge
from beaunity.category.models import Category
from beaunity.comment.models import Comment


UserModel = get_user_model()

creator1 = UserModel.objects.get(pk=1)
creator2 = UserModel.objects.get(pk=2)
creator3 = UserModel.objects.get(pk=3)
creator4 = UserModel.objects.get(pk=4)
creator5 = UserModel.objects.get(pk=5)
creator6 = UserModel.objects.get(pk=6)
creator7 = UserModel.objects.get(pk=7)

event_content_type = ContentType.objects.get_for_model(Event)
challenge_content_type = ContentType.objects.get_for_model(Challenge)
post_content_type = ContentType.objects.get_for_model(Post)

comments_data = [
    {
        "created_by" : creator4,
        "content_type": event_content_type,
        "object_id": 1,
        "content" : "That's very nice event!!"
    },
    {
        "created_by" : creator5,
        "content_type": event_content_type,
        "object_id": 1,
        "content" : "I consider joining, that would be very interesting!!"
    },
    {
        "created_by": creator3,
        "content_type": event_content_type,
        "object_id": 3,
        "content": "Count me in!"
    },
    {
        "created_by": creator4,
        "content_type": event_content_type,
        "object_id": 3,
        "content": "Are there going to be goodie bags?"
    },
    {
        "created_by": creator6,
        "content_type": event_content_type,
        "object_id": 4,
        "content": "This book has been on my to do list for ageeees"
    },
    {
        "created_by": creator2,
        "content_type": challenge_content_type,
        "object_id": 1,
        "content": "I'be been feeling lazy lately, so this could be a good way to energise!!"
    },
    {
        "created_by": creator4,
        "content_type": challenge_content_type,
        "object_id": 1,
        "content": "I send the link so my bestfriend so we could do it together ;))) *excited*"
    },
    {
        "created_by": creator5,
        "content_type": challenge_content_type,
        "object_id": 2,
        "content": "I could join with some tips, I have been journaling since i was 8."
    },
    {
        "created_by": creator3,
        "content_type": challenge_content_type,
        "object_id": 3,
        "content": "This is so motivating"
    },
    {
        "created_by": creator3,
        "content_type": challenge_content_type,
        "object_id": 4,
        "content": "Ive read so many good reviews of doing retinol, but i have always been scared to try. "
    },
    {
        "created_by": creator5,
        "content_type": challenge_content_type,
        "object_id": 4,
        "content": "There is nothing scary, you just have to begin with the smallest concentration of retinol in your serum."
    },
    {
        "created_by": creator6,
        "content_type": challenge_content_type,
        "object_id": 4,
        "content": "I can definitely see myself doing this challenge."
    },
]



for c in comments_data:
    comment = Comment.objects.create(**c)

    print(f"Created comment from user {c["created_by"]}.")