from django.contrib.auth import get_user_model
from beaunity.event.models import Event
from beaunity.category.models import Category

User = get_user_model()

# Getting the creators - Organizer Group
creator1 = User.objects.get(pk=3)

# Getting some categories
category_mindset = Category.objects.get(title="Mindset & Mental Wellness")
category_morning = Category.objects.get(title="Morning Routine")
category_style = Category.objects.get(title="Style & Confidence")
category_self_care = Category.objects.get(title="Self-Care & Pampering")
category_health = Category.objects.get(title="Health & Nutrition")
category_product = Category.objects.get(title="Product Reviews")

# Defining events
event_data = [
    {
        "title": "Sunday Self-Care Rituals",
        "poster_image": "image/upload/v1750749413/acsjv0zstea7cvxsz7z5.png",
        "details": "<p>Join us every Sunday for a cozy, slow-paced online gathering dedicated to self-care. This event is perfect for winding down your weekend and sharing or discovering self-care practices that nourish both skin and soul. Amira will walk us through her evening ritual&mdash;from facial steaming to gratitude journaling&mdash;followed by an open mic session where members can share their routines or ask for tips. Cameras off or on&mdash;come as you are! Highlights: - Skin care demonstration (10 mins) - Guided reflection prompt - Share-your-ritual circle - Curated resource list by the host</p>",
        "is_online": True,
        "city": "",
        "location": "",
        "meeting_link": "https://us02web.zoom.us/j/86543210987?pwd=a1b2C3d4Ef",
        "start_time": "2025-07-19 07:00:00.000000 +00:00",
        "end_time": "2025-07-19 10:00:00.000000 +00:00",
        "is_public": False,
        "is_new": False,
        "created_by": creator1,
        "categories": [
            category_self_care,
            category_morning,
            category_health,
        ],
    },
    {
        "title": "Let’s Talk Toners: Product Reviews Night",
        "poster_image": "image/upload/v1750749750/cwiq9xuc0owqmaddwhe2.webp",
        "details": "<p>Toners - do you love them, or skip them? &nbsp;</p>\n<p>&nbsp;</p>\n<p>Kai Rivera, known for her evidence-based YouTube reviews, will lead this fun and informative product review session. Participants can join in to share what&rsquo;s worked (or didn&rsquo;t), ask for recommendations, or learn about the science behind various formulas. Bring your favorites- or your fails.&nbsp;&nbsp;</p>\n<p>&nbsp;</p>\n<p><strong>Highlights:</strong></p>\n<p>- Quick intro to toner types and ingredients</p>",
        "is_online": False,
        "city": "Varna",
        "location": "ul. 'Sveti Pimen Zografski' 17, 1172 Sofia, Bulgaria",
        "meeting_link": "",
        "start_time": "2025-08-12 08:00:00.000000 +00:00",
        "end_time": "2025-08-12 13:00:00.000000 +00:00",
        "is_public": False,
        "is_new": False,
        "created_by": creator1,
        "categories": [
            category_product
        ],
    },
    {
        "title": "L'oreal: Promo Brunch",
        "poster_image": "image/upload/v1750831951/xmqupw6qiv4c9rfeiibl.jpg",
        "details": "<p>Join us for an exclusive L&#39;Or&eacute;al Promo Brunch, where beauty meets indulgence! 🍾✨ Enjoy a relaxing morning with delicious bites, refreshing drinks, and early access to L&#39;Or&eacute;al&rsquo;s latest product launches and special offers. Chat with beauty experts, get free samples, and be one of the first to try our new collections. Whether you&#39;re a makeup lover or skincare enthusiast, this is the perfect way to treat yourself.</p>",
        "is_online": False,
        "city": "Sofia",
        "location": "bul Bulgariq 25, Bg",
        "meeting_link": "",
        "start_time": "2025-08-22 09:00:00.000000 +00:00",
        "end_time": "2025-08-22 14:00:00.000000 +00:00",
        "is_public": True,
        "is_new": False,
        "created_by": creator1,
        "categories": [
            category_morning,
            category_product,
            category_style,
            category_self_care
        ],
    },
    {
        "title": "Book Club: Atomic Habits by James Clear",
        "poster_image": "image/upload/v1751488192/event_images/atomic_habits_v3cwgl.jpg",
        "details": "<p><strong>Join us for an engaging Book Club session where we dive into <em>Atomic Habits</em> by James Clear.</strong></p>\n<p>&nbsp;</p>\n<p>Discover practical strategies to build good habits, break bad ones, and transform your life one small step at a time.</p>\n<p>Whether you&rsquo;re new to habit-building or looking to refine your approach, this discussion will offer valuable insights and motivation. Come ready to share your thoughts, ask questions, and connect with fellow readers!</p>\n<p>&nbsp;</p>\n<h3><em>Event Timeline (2 hours)</em></h3>\n<p><strong>18:00 &ndash; 18:10</strong> &mdash; Welcome &amp; introductions</p>\n<p>- Briefly introduce everyone and share why you chose <em>Atomic Habits</em></p>\n<p><strong>18:10 &ndash; 19:00</strong>&nbsp;&mdash; Overview of key concepts</p>\n<p>- Discuss James Clear&rsquo;s main ideas: habit stacking, the 4 laws of behavior change, etc.</p>\n<p><strong>19:00 &ndash; 20:00</strong>&nbsp;&mdash; Group discussion</p>\n<p>- Share personal experiences with habits</p>\n<p>- Talk about which strategies from the book resonate most</p>\n<p><strong>20:00 &ndash; 20:15</strong> &mdash; Break</p>\n<p><strong>20:15 &ndash; 20:45</strong> &mdash; Deep dive into a specific chapter or technique</p>\n<p>- Pick a chapter or concept (e.g., habit tracking) and discuss in detail</p>\n<p><strong>20:45 &ndash; 21:00</strong> &mdash; Wrap-up &amp; next steps</p>\n<p>- Summarize takeaways</p>\n<p>- Plan next meeting/book</p>\n<p>- Q&amp;A</p>",
        "is_online": False,
        "city": "Veliko Tarnovo",
        "location": "Marno Pole Park, Veliko Tarnovo, Bulgaria",
        "meeting_link": "",
        "start_time": "2025-08-13 16:00:00.000000 +00:00",
        "end_time": "2025-08-13 19:00:00.000000 +00:00",
        "is_public": True,
        "is_new": False,
        "created_by": creator1,
        "categories": [
            category_mindset
        ],
    },
]


# Creating and assigning categories
for data in challenge_data:
    categories = data.pop("categories")
    challenge = Challenge.objects.create(**data)
    challenge.categories.set(categories) #setting M2M relationships
    print(f"✅ Created challenge: {challenge.title}")


# Assigning attendees
event = Event.objects.get(pk=1)
event.attendees.add(UserModel.objects.get(pk=1))
event.attendees.add(UserModel.objects.get(pk=2))
event.attendees.add(UserModel.objects.get(pk=3))

event.save()

event = Event.objects.get(pk=2)
event.attendees.add(UserModel.objects.get(pk=1))
event.attendees.add(UserModel.objects.get(pk=2))

event.save()

event = Event.objects.get(pk=3)
event.attendees.add(UserModel.objects.get(pk=1))
event.attendees.add(UserModel.objects.get(pk=2))
event.attendees.add(UserModel.objects.get(pk=5))


print("🎉 All events seeded successfully.")
