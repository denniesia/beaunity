from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from django.urls import reverse

from beaunity.category.models import Category
from beaunity.category.views import CategoryOverviewView
from beaunity.common.mixins import UserModel

UserModel = get_user_model()

class TestsCategoryEditView(TestCase):
    def setUp(self):
        Group.objects.get_or_create(name='User')
        self.user = UserModel.objects.create_user(
            username='normaluser',
            email='normaluser@test.bg',
            password='asdfskm2!',
        )
        self.staff = UserModel.objects.create_user(
            username='staffuser',
            email='staffuser@test.bg',
            password='dfgm!2'
        )
        permission = Permission.objects.get(codename='change_category')
        self.staff.user_permissions.add(permission)
        self.staff.save()
        self.category = Category.objects.create(
            title='Test Category',
            description='Test Description',
            image=SimpleUploadedFile(
                name='test.gif',
                content=(
                    b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
                    b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
                    b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01'
                    b'\x00;'
            ),
            content_type='image/gif',
            ),
            created_by=self.staff,
        )

        self.url = reverse('category-edit', kwargs={'category_slug': self.category.slug})

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 202)
        self.assertIn('/login/', response.url )

    def test_get_edit_category_page_with_staff_user(self):
        self.client.login(
            username='staffuser',
            password='dfgm!2'
        )
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category-edit.html')

    def test_change_category_title_success(self):
        self.client.login(
            username='staffuser',
            password='dfgm!2'
        )
        form_data = {
            'title': 'Changed Title',
            'description': self.category.description,
            'image': SimpleUploadedFile(
                name='test.gif',
                content=(
                    b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
                    b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
                    b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01'
                    b'\x00;'
                ),
                content_type='image/gif',
            ),
            'created_by': self.staff,
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('category-overview'))

        self.category.refresh_from_db()
        self.assertEqual(self.category.title, 'Changed Title')
        self.assertEqual(self.category.description, 'Test Description')