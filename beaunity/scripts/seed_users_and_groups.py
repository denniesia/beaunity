import os
from tokenize import group

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beaunity.settings")
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from beaunity.accounts.models import Profile

UserModel = get_user_model()

# # === STEP 1: Create Groups ===
#
# GROUP_NAMES = ["Moderator", "Organizer", "Superuser", "User"]
#
# for group_name in GROUP_NAMES:
#     Group.objects.get_or_create(name=group_name)
# print("✅ Groups created.")

# # === STEP 2: Create Users ===
#
# users = [
#     {
#         "email": "alice.smith@example.com",
#         "username": "alice_s",
#         "password": "Skincare#92",
#         "profile": {
#             "first_name": "Alice",
#             "last_name": "Smith",
#             "date_of_birth": "1990-01-01",
#             "location": "New York",
#             "bio": "Loves skincare and trying new serums.",
#             "skin_type": "Dry Skin"
#         }
#     },
#     {
#         "email": "b.johnson@example.com",
#         "username": "bri_j",
#         "password": "Glow_Up!18",
#         "profile": {
#             "first_name": "Brianna",
#             "last_name": "Johnson",
#             "date_of_birth": "1993-06-15",
#             "location": "Los Angeles",
#             "bio": "Into natural beauty and K-beauty trends.",
#             "skin_type": ""
#         }
#     },
#     {
#         "email": "carolina.lee@example.com",
#         "username": "caro_lee99",
#         "password": "Tr3ndySkin*",
#         "profile": {
#             "first_name": "Carolina",
#             "last_name": "Lee",
#             "date_of_birth": "2002-11-23",
#             "location": "Chicago",
#             "bio": "Experimenting with different moisturizers.",
#             "skin_type": "Oily Skin"
#              },
#            },
#        {
#         "email": "danielle.m@example.com",
#         "username": "dani.elle",
#         "password": "Be@utyR0cks",
#         "profile": {
#             "first_name": "Danielle",
#             "last_name": "",
#             "date_of_birth": "2004-04-04",
#             "location": "",
#             "bio": "This is my bio and this is my pofile, helloo there ",
#             "skin_type": "Normal Skin"
#               }
#            },
#        {
#         "email": "roxane.bauer@example.com",
#         "username": "roxy_foxy",
#         "password": "CmbSkin_L0ve",
#         "profile": {
#             "first_name": "",
#             "last_name": "",
#             "date_of_birth": "2000-08-03",
#             "location": "",
#             "bio": "",
#             "skin_type": ""
#               }
#           },
# ]
#
# #  === STEP 3: Populate Profile Data ===
#
# for u in users:
#     user = UserModel.objects.create_user(
#         email=u["email"],
#         username=u["username"],
#         password=u["password"],
#         is_staff=u.get("is_staff", False),
#         is_superuser=u.get("is_superuser", False),
#     )
#
#
#     profile_data = u.get("profile", {})
#     for key, value in profile_data.items():
#         setattr(user.profile, key, value)
#     user.profile.save()
#
#     print(f"Created user and profile for: {user.email}")


# #  === STEP 4: Define Group Belonging ===

# user = UserModel.objects.get(username="bri_j")
# group = Group.objects.get(name="Superuser")
# user.groups.add(Group.objects.get(name="group"))
# user.is_superuser = True
# user.is_staff = True
# user.save()
#
#print(f"User '{user}' belongs to Group '{group}'")

# user = UserModel.objects.get(username="alice_s")
# group = Group.objects.get(name="Moderator")
# user.groups.add(group)
# user.is_staff = True
# user.save()
#
#print(f"User '{user}' belongs to Group '{group}'")

# user = UserModel.objects.get(username="caro_lee99")
# group = Group.objects.get(name="Organizer")
# user.groups.add(group)
# user.is_staff = True
# user.save()
#
#print(f"User '{user}' belongs to Group '{group}'")


# # Optional: clear data (use with caution in dev only)
# UserModel.objects.all().delete()
# Profile.objects.all().delete()