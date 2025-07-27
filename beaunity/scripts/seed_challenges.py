from django.contrib.auth import get_user_model
from beaunity.challenge.models import Challenge
from beaunity.category.models import Category

User = get_user_model()

# Getting the creators - User Group
creator1 = User.objects.get(pk=4)
creator2 = User.objects.get(pk=5)

# Getting some categories
category_mindset = Category.objects.get(title="Mindset & Mental Wellness")
category_morning = Category.objects.get(title="Morning Routine")
category_journey = Category.objects.get(title="My Journey")
category_style = Category.objects.get(title="Style & Confidence")

# Defining challenges
challenge_data = [
    {
        "title": "Morning Energy Boost",
        "poster_image": "image/upload/v1751694985/vbuywip9scpqhzki7ze6.jpg",
        "details": "<p>I&#39;ve been feeling really sluggish in the mornings lately &mdash; like I&#39;m dragging myself out of bed and rushing into the day without really waking up. So I created this <strong>challenge </strong>to give myself a softer, more intentional start.</p><p>&nbsp;</p><p>My goal is simple: <strong>every morning for the next week, I&rsquo;ll do a 10-minute stretch, drink a big glass of water, and write down just one thing I&rsquo;m grateful for.</strong> It doesn&rsquo;t have to be deep or perfect &mdash; I just want to center myself before the day begins.I will set the end time in 10 weeks.&nbsp;</p><p>I hope this helps me feel more energized and positive in the mornings. And honestly, I think starting the day with gratitude might shift my whole mindset. Anyone want to join me? I would be great if I find people that would like to join me.</p>",
        "difficulty": "Beginner",
        "is_online": True,
        "meeting_link": "",
        "created_by": creator1,
        "categories": [category_journey],
        "city": "",
        "location": "",
        "start_time": "2025-08-15 06:00:00.000000 +00:00",
        "end_time": "2025-10-24 06:00:00.000000 +00:00",
        "is_new": False,
        "is_approved": True,
    },
    {
        "title": "Write It Out",
        "poster_image": "image/upload/v1751867835/event_images/journaling_we77gm.png",
        "details": "Lately, my mind feels like a browser with too many tabs open. I&#39;m carrying around little worries, thoughts, to-dos &mdash; and it&#39;s all just... noisy. So I&rsquo;m starting this journaling challenge to help clear some space in my head.&nbsp;&nbsp; For 7 days, I&rsquo;ll spend 10 minutes each evening writing whatever&rsquo;s on my mind. No pressure to be profound &mdash; just a brain dump, some reflection, or even a short story if I feel like it. &nbsp; I want to reconnect with myself and slow down a bit.I believe writing things out will help me sleep better and be more intentional with how I move through the week. If you&rsquo;re also feeling overwhelmed or scattered, maybe this can help you too.",
        "is_online": True,
        "meeting_link": "https://us02web.zoom.us/j/86543210987?pwd=a1b2C3d4Ef",
        "city": "",
        "location": "",
        "start_time": "2025-08-10 05:30:00.000000 +00:00",
        "end_time": "2025-08-16 21:59:00.000000 +00:00",
        "is_new": False,
        "difficulty": "Beginner",
        "is_approved": True,
        "created_by": creator1,
        "categories": [category_mindset, category_journey],
    },
    {
        "title": "Axing My Finals",
        "poster_image": "image/upload/v1751976301/event_images/pexels-olia-danilevich-8093032_xo6oop.jpg",
        "details": "p>Final exams can feel overwhelming, but with the right mindset and a solid plan, I can tackle them with confidence. This challenge is about staying consistent, reducing stress, and giving my best shot to crush my finals and come out stronger.</p><p>Steps:</p><ol><li><p><strong>Set Clear Goals</strong> &ndash; Identify what I want to achieve for each subject.</p></li><li><p><strong>Create a Study Plan</strong> &ndash; Break down topics into manageable chunks and schedule them weekly.</p></li><li><p><strong>Stay Consistent</strong> &ndash; Stick to the schedule and track daily progress.</p></li><li><p><strong>Practice &amp; Review</strong> &ndash; Do mock exams, practice questions, and weekly reviews.</p></li><li><p><strong>Take Care of Myself</strong> &ndash; Get enough sleep, eat well, and include short breaks and exercise.</p></li><li><p><strong>Stay Positive</strong> &ndash; Use motivation techniques like affirmations, study playlists, or rewards.</p></li></ol>",        "start_time": "2025-05-05 06:00:00+00:00",
        "is_online": True,
        "meeting_link": "",
        "city": "",
        "location": "",
        "start_time": "2025-05-05 06:00:00.000000 +00:00",
        "end_time": "2025-07-13 06:00:00.000000 +00:00",
        "is_new": False,
        "difficulty": "Beginner",
        "is_approved": True,
        "created_at": "2025-07-08 12:03:40.860457 +00:00",
        "end_time": "2025-07-13 06:00:00+00:00",
        "difficulty": "Beginner",
        "created_by": creator2,
        "categories": [category_style],
    },
    {
        "title": "Glow-Up: Retinol Routine",
        "poster_image": "image/upload/v1751795331/event_images/retinol_pp1zwr.webp",
        "details": "<p>I&rsquo;ve decided it&rsquo;s time to commit to a consistent retinol routine &mdash; not just for the skin benefits, but as an act of self-discipline and self-care. This challenge is simple: apply retinol <strong>2 times a week</strong> for the next 4 weeks.</p>\n<p>Why? Because I&rsquo;m tired of being inconsistent with my skincare goals. Retinol has been sitting in my drawer long enough &mdash; it&rsquo;s time to finally use it properly and see what it can really do. I want to improve my skin texture, reduce breakouts, and support long-term glow and resilience.</p>\n<p>Joining this challenge means building a habit, learning patience, and tracking small but meaningful progress. Let&rsquo;s commit to a routine that supports our future selves!</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>\n<p><strong>💡 <em>Tips:</em></strong></p>",
        "is_online": True,
        "meeting_link": "",
        "city": "",
        "location": "",
        "start_time": "2025-07-21 09:46:00.000000 +00:00",
        "end_time": "2025-08-03 09:46:00.000000 +00:00",
        "is_new": False,
        "difficulty": "Beginner",
        "is_approved": True,
        "created_by": creator2,
        "categories": [category_morning],
    },
    {
        "title": "1 Hour Daily Reading Challenge",
        "poster_image": "image/upload/v1751870238/event_images/books.jpg_ggrdvi.png",
        "details": "Let&rsquo;s be honest &mdash; we scroll too much and read too little. This challenge is your invitation to slow down and reconnect with a deeper, more focused version of yourself. &nbsp; Lately, I&rsquo;ve been feeling like my attention span is shrinking. I scroll endlessly, multitask everything, and at the end of the day, I often feel mentally cluttered but not actually enriched. I miss feeling inspired. I miss learning for the joy of it. So I&rsquo;m starting something simple, but powerful:&nbsp;Hour of Reading Every Day Challenge! &nbsp; Reading every day can: Boost concentration and reduce stress 🧘&zwj;♀️ Expand your knowledge and vocabulary 💡 Spark your imagination and creativity ✨ Help you sleep better by disconnecting from screens 😴 Make you feel productive and fulfilled 📈 &nbsp; Why I&rsquo;m Doing This I want to reclaim my focus in a world of constant distractions. I want to trade screen time for something more nourishing. I want to feel grounded, curious, and inspired again. I want to remember what it&rsquo;s like to read something that truly moves me. &nbsp; Reading has always been a quiet act of self-care for me &mdash; and I&rsquo;m ready to bring that back.",
        "is_online": True,
        "meeting_link": "https://us02web.zoom.us/j/86543210987?pwd=a1b2C3d4Ef",
        "city": "",
        "location": "",
        "start_time": "2025-07-18 06:00:00.000000 +00:00",
        "end_time": "2025-08-11 06:00:00.000000 +00:00",
        "is_new": False,
        "difficulty": "Beginner",
        "is_approved": False,
        "created_by": creator2,
        "categories": [category_morning, category_mindset],
    },
]

# Creating and assigning categories
for data in challenge_data:
    categories = data.pop("categories")
    challenge = Challenge.objects.create(**data)
    challenge.categories.set(categories) #setting M2M relationships
    print(f"✅ Created challenge: {challenge.title}")


# Assigning attendees
challenge = Challenge.objects.get(pk=1)
challenge.attendees.add(UserModel.objects.get(pk=1))
challenge.attendees.add(UserModel.objects.get(pk=2))
challenge.attendees.add(UserModel.objects.get(pk=3))

challenge.save()

challenge = Challenge.objects.get(pk=2)
challenge.attendees.add(UserModel.objects.get(pk=2))
challenge.attendees.add(UserModel.objects.get(pk=3))

challenge.save()

challenge = Challenge.objects.get(pk=3)
challenge.attendees.add(UserModel.objects.get(pk=2))
challenge.attendees.add(UserModel.objects.get(pk=3))
challenge.attendees.add(UserModel.objects.get(pk=4))
challenge.attendees.add(UserModel.objects.get(pk=5))

challenge.save()

challenge = Challenge.objects.get(pk=4)
challenge.attendees.add(UserModel.objects.get(pk=3))


challenge.save()
print("🎉 All challenges seeded successfully.")
