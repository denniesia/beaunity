from datetime import date
from unittest import expectedFailure

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from prompt_toolkit.key_binding.bindings.named_commands import self_insert

from beaunity.accounts.models import Profile

UserModel = get_user_model()


class TestProfile(TestCase):
    def setUp(self):
        Group.objects.create(name="User")
        self.user = UserModel.objects.create_user(
            username="test", email="test@test.com", password="test123!A"
        )

    def test__full_name_property(self):

        profile = self.user.profile
        profile.first_name = "Test"

        profile.save()

        self.assertEqual(profile.full_name, "Test")

    def test__age_property(self):
        profile = self.user.profile
        profile.date_of_birth = date(1996, 11, 25)
        profile.save()

        expected = (
            date.today().year
            - 1996
            - ((date.today().month, date.today().day) < (11, 25))
        )

        self.assertEqual(profile.age, expected)
