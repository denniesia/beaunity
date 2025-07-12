from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from beaunity.category.models import Category
from beaunity.post.models import Post

UserModel = get_user_model()


class TestsPostModel(TestCase):
    def test_valid__str__method(self):
        Group.objects.get_or_create(name="User")
        user = UserModel.objects.create_user(
            username="test", email="test@test.bg", password="test1332!"
        )

        category = Category.objects.create(
            image=SimpleUploadedFile(
                name="test.gif",
                content=(
                    b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00"
                    b"\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00"
                    b"\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01"
                    b"\x00;"
                ),
                content_type="image/gif",
            ),
            title="Test Category",
            description="Test Description",
            created_by=user,
        )

        post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            category=category,
            created_by=user,
        )

        self.assertEqual(str(post), "Test Post")
