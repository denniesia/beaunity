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
    # Comments on Events
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

    # Comments on Challenges
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

    # Comments on Posts
    {
        "created_by": creator6,
        "content_type": post_content_type,
        "object_id": 5,
        "content": "Absolutely. I constantly feel like I don’t belong, especially at work—even when I’m doing well. What’s helped a bit is keeping a folder of positive feedback to look at when doubt creeps in."
    },
    {
        "created_by": creator3,
        "content_type": post_content_type,
        "object_id": 5,
        "content": "Yes, you’re not alone. I try to remind myself that growth often feels uncomfortable and that even the most accomplished people struggle with this."
    },
    {
        "created_by": creator2,
        "content_type": post_content_type,
        "object_id": 5,
        "content": "All the time! I’ve found talking to mentors or trusted friends helps ground me. Sometimes just hearing 'you’re not crazy, I feel that too' makes a big difference."
    },
    {
        "created_by": creator1,
        "content_type": post_content_type,
        "object_id": 4,
        "content": "I set alarms every hour as a reminder to drink—it sounds simple, but it really works! Also, using a fun water bottle makes it feel less like a chore."
    },
    {
        "created_by": creator2,
        "content_type": post_content_type,
        "object_id": 4,
        "content": "Cucumber + mint water is a game changer for me. Refreshing and it actually makes me want to keep sipping!"
    },
    {
        "created_by": creator3,
        "content_type": post_content_type,
        "object_id": 4,
        "content": "I use an app called Plant Nanny—it turns hydration into a game where you keep a plant alive by drinking water. Weirdly effective!"
    },
    {
        "created_by": creator5,
        "content_type": post_content_type,
        "object_id": 4,
        "content": "I prep a big jug of fruit-infused water every morning (lemon, berries, basil, etc.). It feels fancy and makes me reach for it more than plain water."
    },
    {
        "created_by": creator3,
        "content_type": post_content_type,
        "object_id": 1,
        "content": "Overnight oats with chia seeds, Greek yogurt, and berries—takes 5 minutes to prep the night before and keeps me full for hours."
    },
    {
        "created_by": creator5,
        "content_type": post_content_type,
        "object_id": 1,
        "content": "Scrambled eggs with spinach on whole grain toast. Quick, protein-packed, and actually satisfying until lunchtime!"
    },
    {
        "created_by": creator1,
        "content_type": post_content_type,
        "object_id": 7,
        "content": "Definitely applying vitamin C serum—feels like a little glow boost to start the day!"
    },
    {
        "created_by": creator2,
        "content_type": post_content_type,
        "object_id": 6,
        "content": "Yes!! Pink has such a powerful vibe—confident, playful, and bold all at once. Love that you felt it!"
    },

]

# Creating comments

for c in comments_data:
    comment = Comment.objects.create(**c)

    print(f"Created comment from user {c["created_by"]}.")

# Editing created_at on comments:

comment = Comment.objects.get(pk=1)
comment.created_at = timezone.now() - timedelta(minutes=5)
comment.save()

comment = Comment.objects.get(pk=3)
comment.created_at = timezone.now() - timedelta(minutes=2)
comment.save()

comment = Comment.objects.get(pk=6)
comment.created_at = timezone.now() - timedelta(minutes=5)
comment.save()

comment = Comment.objects.get(pk=10)
comment.created_at = timezone.now() - timedelta(minutes=30)
comment.save()

comment = Comment.objects.get(pk=11)
comment.created_at = timezone.now() - timedelta(minutes=3)
comment.save()

comment = Comment.objects.get(pk=13)
comment.created_at = timezone.now() - timedelta(minutes=30)
comment.save()

comment = Comment.objects.get(pk=14)
comment.created_at = timezone.now() - timedelta(minutes=3)
comment.save()

comment = Comment.objects.get(pk=16)
comment.created_at = timezone.now() - timedelta(minutes=30)
comment.save()

comment = Comment.objects.get(pk=17)
comment.created_at = timezone.now() - timedelta(minutes=13)
comment.save()


comment = Comment.objects.get(pk=18)
comment.created_at = timezone.now() - timedelta(minutes=10)
comment.save()


comment = Comment.objects.get(pk=16)
comment.created_at = timezone.now() - timedelta(minutes=3)
comment.save()

comment = Comment.objects.get(pk=20)
comment.created_at = timezone.now() - timedelta(hour=1)
comment.save()

comment = Comment.objects.get(pk=21)
comment.created_at = timezone.now() - timedelta(minutes=47)
comment.save()

print("🎉 All comments seeded successfully.")