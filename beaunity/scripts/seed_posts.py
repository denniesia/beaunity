import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beaunity.settings")
django.setup()

from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from beaunity.post.models import Post
from beaunity.category.models import Category

User = get_user_model()

# Getting the creators - Organizer Group
creator1 = User.objects.get(pk=4)
creator2 = User.objects.get(pk=5)

# Getting some categories
category_mindset = Category.objects.get(title="Mindset & Mental Wellness")
category_morning = Category.objects.get(title="Morning Routine")
category_style = Category.objects.get(title="Style & Confidence")
category_self_care = Category.objects.get(title="Self-Care & Pampering")
category_health = Category.objects.get(title="Health & Nutrition")
category_product = Category.objects.get(title="Product Reviews")
category_ask = Category.objects.get(title="Ask the community")

# Defining posts

posts_data = [
    {
        "banner": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=2053&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "title": "Quick & Healthy Breakfast Ideas?",
        "content": "Looking for nutritious breakfast options that are quick to prepare and keep you full until lunch. What do you eat in the morning that fuels your day?",
        "is_approved": True,
        "category_id": category_morning,
        "created_by": creator1,
    },
    {
        "banner": "https://plus.unsplash.com/premium_photo-1684407616442-8d5a1b7c978e?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "title": "Morning Routine Must-Haves?",
        "content": "What are your holy grail skincare products for a glowing morning routine? I’m trying to build a routine that hydrates and protects throughout the day. Bonus points for SPF recommendations!",
        "is_approved": True,
        "category_id": category_self_care,
        "created_by": creator1,
    },
    {
        "banner": "https://images.unsplash.com/photo-1607874963930-2edecc67a25a?q=80&w=2052&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "title": "Supplements You Swear By?",
        "content": "From collagen to magnesium—what supplements have you noticed a real difference with? Share your favorite brands and how they’ve helped you!",
        "is_approved": False,
        "category_id": category_health,
        "created_by": creator1,
    },
    {
        "banner": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTV2XbtEQpuQfuebx99luGnezHZzY63TludZw&s",
        "title": "Hydration Tips for Busy Days",
        "content": "I always forget to drink water throughout the day. Anyone have creative ways to stay hydrated—like infusions or apps? Let’s share ideas!",
        "is_approved": True,
        "category_id": category_health,
        "created_by": creator1,
    },
    {
        "banner": "",
        "title": "Imposter Syndrome Struggles",
        "content": "Anyone else struggling with imposter syndrome? Whether it's at work, school, or just life in general—how do you manage those self-doubt moments?",
        "is_approved": True,
        "category_id": category_ask,
        "created_by": creator1,
    },
    {
        "banner": "",
        "title": "How Wearing My Favorite Color Boosted My Mood",
        "content": "Tried an all-pink outfit today and felt so empowered. Color therapy is real 💖✨",
        "is_approved": True,
        "category_id": category_style,
        "created_by": creator2,
    },
    {
        "banner": "",
        "title": "Skincare Routine",
        "content": "What’s your favorite morning skincare step?",
        "is_approved": True,
        "category_id": category_morning,
        "created_by": creator2,
    },
    {
        "banner": "https://img01.ztat.net/article/spp-media-p1/6e1ebdeb671c468eaccfe1ebdad2ee6d/62a00df006004ae39ceca11cf051d527.jpg?imwidth=1800&filter=packshot",
        "title": "SKIN1004 Madagascar Centella Ampoule",
        "content": "Hey guys, has somebody used this serum? I am thinking of buying it because I see a lot of positive feedback on tik tok but i am not quite sure. I have dry skin.",
        "is_approved": True,
        "category_id": category_product,
        "created_by": creator2,
    },
    {
        "banner": "",
        "title": "Confidence Boost",
        "content": "What’s one habit that makes you feel confident?",
        "is_approved": False,
        "category_id": category_product,
        "created_by": creator2,
    },
    {
        "banner": "",
        "title": "Self-Care Tips",
        "content": "How do you unwind after a stressful day?",
        "is_approved": False,
        "category_id": category_ask,
        "created_by": creator2,
    },
]


# Creating posts
for data in posts_data:
    post = Post.objects.create(**data)

    print(f"✅ Created post: {post.title}")

#Defining some created_at fields
post1 = Post.objects.get(id=1)
post1.created_at = timezone.now() - timedelta(days=3)
post1.save()

post2 = Post.objects.get(id=2)
post2.created_at = timezone.now() - timedelta(days=3, minutes=33)
post2.save()


post3 = Post.objects.get(id=3)
post3.created_at = timezone.now() - timedelta(days=5, minutes=5)
post3.save()

post4 = Post.objects.get(id=4)
post4.created_at = timezone.now() - timedelta(days=4, minutes=44)
post4.save()

post5 = Post.objects.get(id=5)
post5.created_at = timezone.now() - timedelta(days=5, minutes=55)
post5.save()

post6 = Post.objects.get(id=6)
post6.created_at = timezone.now() - timedelta(days=6, minutes=8)
post6.save()

post7 = Post.objects.get(id=7)
post7.created_at = timezone.now() - timedelta(days=12, minutes=8)
post7.save()

post8 = Post.objects.get(id=8)
post8.created_at = timezone.now() - timedelta(days=12, minutes=3)
post8.save()

print("🎉 All posts seeded successfully.")