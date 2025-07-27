# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beaunity.settings")
# django.setup()
#
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
# from beaunity.category.models import Category
#
# UserModel = get_user_model()
#
#
# categories = [
#     {
#         "title": "Mindset & Mental Wellness23",
#         "description": "Discuss mindfulness, affirmations, journaling, and emotional self-care.",
#         "created_by_id": 1,
#         "image": "mindset-mental-wellness,image/upload/v1750502384/category_images/growth-mindset_iaivyz.png",
#
#     },
#     {
#         "title": "Health & Nutrition",
#         "description": "Explore healthy eating habits, hydration, supplements, and wellness tips.",
#         "created_by_id": 1,
#         "image": "image/upload/v1750502702/category_images/check-up_n08eql.png",
#     },
#     {
#         "title": "Morning Routine",
#         "description": "Share tips and rituals to start your day with focus and energy.",
#         "created_by_id": 1,
#         "image": "image/upload/v1750502426/category_images/morning-coffee_mmppzf.png",
#     },
#     {
#         "title": "Night Routine",
#         "description": "Discuss winding-down habits, nighttime skincare, and preparing for restful sleep.",
#         "created_by_id": 1,
#         "image": "image/upload/v1750502489/category_images/moon_bkfney.png",
#     },
#     {
#         "title": "My Journey",
#         "description": "A personal space to share milestones, progress, setbacks, or transformations..",
#         "created_by_id": 1,
#         "image": "image/upload/v1750502454/category_images/journal_du6u8b.png",
#     },
#     {
#         "title": "Ask the community",
#         "description": "Ask questions, get advice, or crowdsource recommendations from others.",
#         "created_by_id": 1,
#         "image": "image/upload/v1750501903/category_images/question_xerf5t.png",
#     },
#     {
#         "title": "Self-Care & Pampering",
#         "description": "Talk about relaxing rituals, self-love practices, and feel-good activities.",
#         "created_by_id": 1,
#         "image": "image/upload/v1750502594/category_images/heart_dnhgip.png",
#     },
#     {
#         "title": "Product Reviews",
#         "description": "Honest thoughts on skincare and wellness products — what worked and what didn’t.",
#         "created_by_id": 1,
#         "image": "image/upload/v1750502535/category_images/beauty-and-cosmetics_xyhryz.png",
#     },
#     {
#         "title": "Style & Confidence",
#         "description": "Share outfit ideas, beauty inspiration, and tips on expressing your personal style with confidence.",
#         "created_by_id": 1,
#         "image": "image/upload/v1750502660/category_images/coat_af4ppe.png",
#     },
# ]
#
#
# for category in categories:
#     Category.objects.create(**category)
#
#     print(f"✅ Category {category['title']} created")
#

# # Optional: clear data
# Category.objects.all().delete()
