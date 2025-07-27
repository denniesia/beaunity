import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beaunity.settings")
django.setup()

from datetime import datetime, timedelta
from django.utils import timezone

from beaunity.category.models import Category
from slugify import slugify


# === Populate Category Data ===
categories_data  = [
    {
        "title": "Mindset & Mental Wellness",
        "description": "Discuss mindfulness, affirmations, journaling, and emotional self-care.",
        "created_by_id": 1,
        "image": "mindset-mental-wellness,image/upload/v1750502384/category_images/growth-mindset_iaivyz.png",
        "slug": "mindset-mental-wellness"

    },
    {
        "title": "Health & Nutrition",
        "description": "Explore healthy eating habits, hydration, supplements, and wellness tips.",
        "created_by_id": 1,
        "image": "image/upload/v1750502702/category_images/check-up_n08eql.png",
        "slug": "health-nutrition"
    },
    {
        "title": "Morning Routine",
        "description": "Share tips and rituals to start your day with focus and energy.",
        "created_by_id": 1,
        "image": "image/upload/v1750502426/category_images/morning-coffee_mmppzf.png",
        "slug": "morning-routine"
    },
    {
        "title": "Night Routine",
        "description": "Discuss winding-down habits, nighttime skincare, and preparing for restful sleep.",
        "created_by_id": 1,
        "image": "image/upload/v1750502489/category_images/moon_bkfney.png",
        "slug": "night-routine"
    },
    {
        "title": "My Journey",
        "description": "A personal space to share milestones, progress, setbacks, or transformations..",
        "created_by_id": 1,
        "image": "image/upload/v1750502454/category_images/journal_du6u8b.png",
        "slug": "my-journey"
    },
    {
        "title": "Ask the community",
        "description": "Ask questions, get advice, or crowdsource recommendations from others.",
        "created_by_id": 1,
        "image": "image/upload/v1750501903/category_images/question_xerf5t.png",
        "slug": "ask-the-community"
    },
    {
        "title": "Self-Care & Pampering",
        "description": "Talk about relaxing rituals, self-love practices, and feel-good activities.",
        "created_by_id": 1,
        "image": "image/upload/v1750502594/category_images/heart_dnhgip.png",
        "slug": "self-care-and-pampering"
    },
    {
        "title": "Product Reviews",
        "description": "Honest thoughts on skincare and wellness products — what worked and what didn’t.",
        "created_by_id": 1,
        "image": "image/upload/v1750502535/category_images/beauty-and-cosmetics_xyhryz.png",
        "slug": "product-reviews"
    },
    {
        "title": "Style & Confidence",
        "description": "Share outfit ideas, beauty inspiration, and tips on expressing your personal style with confidence.",
        "created_by_id": 1,
        "image": "image/upload/v1750502660/category_images/coat_af4ppe.png",
        "slug": "style-confidence"
    },
]


category_instances = [Category(**data) for data in categories_data]
Category.objects.bulk_create(category_instances)
print(f"✅ Categories created")


# # Optional: clear data
# Category.objects.all().delete()
