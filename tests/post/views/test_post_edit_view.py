
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from beaunity.post.models import Post
from beaunity.category.models import Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import Group

UserModel = get_user_model()

class TestsPostEditView(TestCase):
    def setUp(self):
        Group.objects.get_or_create(name='User')

        self.user = UserModel.objects.create_user(
            username='test',
            email='test@test.bg',
            password='test1332!',

        )
        self.superuser = UserModel.objects.create_user(
            username='superuser',
            email='superuser@test.bg',
            password='gsdgs!2dd',
            is_superuser=True,

        )
        self.user.groups.add(Group.objects.get(name='User'))


        self.category = Category.objects.create(
            image=SimpleUploadedFile(
                name='test.gif',
                content=(
                    b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
                    b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
                    b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01'
                    b'\x00;'
                ),
                content_type='image/gif'
            ),
            title='Test Category',
            description='Test Description',
            created_by=self.user
        )

        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            category=self.category,
            created_by=self.user
        )

    def test__get_success_url__for_normal_user(self):
        self.client.login(username='test', password='test1332!')
        response = self.client.post(
            reverse('post-edit', kwargs={'pk': self.post.pk}),
            data={
                'title': 'Updated title',
                'content': 'Updated content',
                'category': self.category.pk,
            }
        )


        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post-details', kwargs={'pk':self.post.pk}))

    def test__get_success_url__for_superuser(self):
        self.client.login(username='superuser', password='gsdgs!2dd')
        response = self.client.post(
            reverse('post-edit', kwargs={'pk': self.post.pk}),
            data={
                'title': 'Updated title',
                'content': 'Updated content',
                'category': self.category.pk,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post-pending'))
