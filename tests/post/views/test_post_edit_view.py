from allauth.account.signals import password_reset
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from django.urls import reverse

from beaunity.category.models import Category
from beaunity.post.forms import AdminPostEditForm, PostEditForm
from beaunity.post.models import Post
from beaunity.post.views import PostEditView

UserModel = get_user_model()


class TestsPostEditView(TestCase):
    def setUp(self):
        Group.objects.get_or_create(name="User")
        Group.objects.get_or_create(name="Superuser")

        self.user = UserModel.objects.create_user(
            username="test",
            email="test@test.bg",
            password="test1332!",
        )
        self.superuser = UserModel.objects.create_user(
            username="superuser",
            email="superuser@test.bg",
            password="gsdgs!2dd",
            is_superuser=True,
        )
        self.user.groups.add(Group.objects.get(name="User"))
        self.superuser.groups.add(Group.objects.get(name="Superuser"))

        self.category = Category.objects.create(
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
            created_by=self.user,
        )

        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            category=self.category,
            created_by=self.user,
        )

    def test__get_success_url__for_normal_user(self):
        self.client.login(username="test", password="test1332!")
        response = self.client.post(
            reverse("post-edit", kwargs={"pk": self.post.pk}),
            data={
                "title": "Updated title",
                "content": "Updated content",
                "category": self.category.pk,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("post-details", kwargs={"pk": self.post.pk})
        )

    def test__get_success_url__for_superuser(self):
        self.client.login(username="superuser", password="gsdgs!2dd")
        response = self.client.post(
            reverse("post-edit", kwargs={"pk": self.post.pk}),
            data={
                "title": "Updated title",
                "content": "Updated content",
                "category": self.category.pk,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("post-pending"))

    def test__test_func_superuser_can_edit(self):
        self.client.login(username="superuser", password="gsdgs!2dd")
        response = self.client.post(reverse("post-edit", kwargs={"pk": self.post.pk}))

        self.assertEqual(response.status_code, 200)

    def test__test_func_other_user_cannot_edit(self):
        other_user = UserModel.objects.create_user(
            username="other_user", email="other_user@test.bg", password="sdfkmlsd!"
        )
        self.client.login(username="other_user", password="sdfkmlsd!")
        response = self.client.post(reverse("post-edit", kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 403)

    def test__admin_gets_right_edit_post_form(self):
        post = Post.objects.create(
            title="Test Post",
            content="Test content",
            category=self.category,
            created_by=self.user,
            is_approved=False,
        )
        request = RequestFactory().get("/")
        request.user = self.superuser

        view = PostEditView()
        view.request = request
        view.kwargs = {"pk": post.pk}
        view.object = post

        form_class = view.get_form_class()

        self.assertEqual(form_class, AdminPostEditForm)

    def test__creator_gets_right_edit_post_form(self):
        post = Post.objects.create(
            title="Test Post",
            content="Test content",
            category=self.category,
            created_by=self.user,
            is_approved=True,
        )
        request = RequestFactory().get("/")
        request.user = self.user

        view = PostEditView()
        view.request = request
        view.kwargs = {"pk": post.pk}
        view.object = post

        form_class = view.get_form_class()

        self.assertEqual(form_class, PostEditForm)
