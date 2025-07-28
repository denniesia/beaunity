import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beaunity.settings")
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from beaunity.accounts.models import Profile

UserModel = get_user_model()

# === STEP 1: Create Users ===

users = [
    {
        "email": "alicia.sim@example.com",
        "username": "alice_s",
        "password": "Skincare#92",
        "is_active": True,
        "profile": {
            "profile_pic": "image/upload/v1753680201/profile_pics/pic_yi0k9m.jpg",
            "first_name": "Alisiq",
            "last_name": "Simova",
            "date_of_birth": "1992-01-01",
            "location": "Sofiq",
            "bio": "Hello this is my profile, have fun.",
            "skin_type": "Dry Skin"
        }
    },
    {
        "email": "b_mladenova@example.com",
        "username": "bilyanaa",
        "password": "Glow_Up!18",
        "is_active": True,
        "profile": {
            "profile_pic": "image/upload/v1753680542/profile_pics/pic2_acoifq.avif",
            "first_name": "Bilyana",
            "last_name": "Mladenova",
            "date_of_birth": "1993-06-15",
            "location": "Varna",
            "bio": "Into natural beauty and K-beauty trends.",
            "skin_type": ""
        }
    },
    {
        "email": "karolina.lee@example.com",
        "username": "caro_lee99",
        "password": "Tr3ndySkin*",
        "is_active": True,
        "profile": {
            "profile_pic": "image/upload/v1751294216/profile_pics/avatar2_el5tyl.avif",
            "first_name": "Karolina",
            "last_name": "Lilova",
            "date_of_birth": "2002-11-23",
            "location": "Shumen",
            "bio": "Experimenting with different moisturizers.",
            "skin_type": "Oily Skin"
        },
    },
    {
        "email": "danielle.m@example.com",
        "username": "dani.elle",
        "password": "Be@utyR0cks",
        "is_active": True,
        "profile": {
            "profile_pic": "image/upload/v1750936500/profile_pics/e35e40c9be86b5b6e46d6503b299c01a_gzelaz.jpg",
            "first_name": "Danielle",
            "last_name": "Elle",
            "date_of_birth": "2004-04-04",
            "location": "",
            "bio": "This is my bio and this is my pofile, helloo there",
            "skin_type": "Normal Skin"
        }
    },
    {
        "email": "roxane@example.com",
        "username": "roxy_foxy",
        "password": "CmbSkin_L0ve",
        "is_active": True,
        "profile": {
            "first_name": "Roksana",
            "last_name": "",
            "date_of_birth": "2000-08-03",
            "location": "",
            "bio": "",
            "skin_type": ""
        }
    },
    {
        "email": "elena_dim@example.com",
        "username": "ellaine",
        "password": "CmbSkin_LoV3",
        "is_active": True,
        "profile": {
            "first_name": "Elena",
            "last_name": "Roskova",
            "date_of_birth": "2002-07-03",
            "location": "Veliko Tarnovo",
            "bio": "",
            "skin_type": "Normal Skin"
        }
    },
    {
        "email": "mariyaa@example.com",
        "username": "mariyaa",
        "password": "LoV3_iT22",
        "is_active": True,
        "profile": {
            "first_name": "Mariya",
            "last_name": "",
            "date_of_birth": "2005-02-03",
            "location": "Sofiq",
            "bio": "I am just browsing around",
            "skin_type": "Normal Skin"
        }
    },
]

#  === STEP 2: Populate Profile Data ===

for u in users:
    user = UserModel.objects.create_user(
        email=u["email"],
        username=u["username"],
        password=u["password"],
        is_staff=u.get("is_staff", False),
        is_superuser=u.get("is_superuser", False),
        is_active=u.get("is_active", False),
    )


    profile_data = u.get("profile", {})
    for key, value in profile_data.items():
        setattr(user.profile, key, value)
    user.profile.save()

    print(f"Created user and profile for: {user.email}")


#  === STEP 3: Define Group Belonging ===

user = UserModel.objects.get(pk=1)
group = Group.objects.get(name="Superuser")
user.groups.add(group)
user.is_superuser = True
user.is_staff = True
user.save()

print(f"User '{user}' belongs to Group '{group}'")

user = UserModel.objects.get(pk=2)
group = Group.objects.get(name="Moderator")
user.groups.add(group)
user.is_staff = True
user.save()

print(f"User '{user}' belongs to Group '{group}'")

user = UserModel.objects.get(pk=3)
group = Group.objects.get(name="Organizer")
user.groups.add(group)
user.is_staff = True
user.save()

print(f"User '{user}' belongs to Group '{group}'")


# # Optional: clear data
# UserModel.objects.all().delete()
# Profile.objects.all().delete()