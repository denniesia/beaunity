from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from django.urls import reverse

from beaunity.category.models import Category
from beaunity.category.views import CategoryOverviewView
from beaunity.common.mixins import UserModel

UserModel = get_user_model()


class TestsCategoryCreateView(TestCase):
    def setUp(self):
        Group.objects.get_or_create(name="User")
        self.user = UserModel.objects.create_user(
            username="normaluser",
            email="test@test.bg",
            password="4354mvo!N",
        )

        self.staff_user = UserModel.objects.create_user(
            username="staffuser",
            email="staff@test.bg",
            password="skdfgmW2!",
        )

        permission = Permission.objects.get(codename="add_category")
        self.staff_user.user_permissions.add(permission)
        self.staff_user.save()

        self.url = reverse("category-create")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 202)
        self.assertIn("/login/", response.url)

    def test_forbidden_if_normal_user(self):
        self.client.login(username="normaluser", password="4354mvo!N")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_get_create_category_page_with_staff_user(self):
        self.client.login(username="staffuser", password="skdfgmW2!")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "category/category-create.html")

    def test_create_category_with_staff_user(self):
        self.client.login(username="staffuser", password="skdfgmW2!")
        test_image = SimpleUploadedFile(
            name="test.gif",
            content=(
                b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00"
                b"\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00"
                b"\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01"
                b"\x00;"
            ),
            content_type="image/gif",
        )
        form_data = {
            "title": "Test title",
            "description": "Test description",
            "image": test_image,
        }

        response = self.client.post(self.url, data=form_data)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse("category-overview"))

        category = Category.objects.get(title="Test title")
        self.assertEqual(category.created_by, self.staff_user)
        self.assertEqual(category.description, "Test description")
