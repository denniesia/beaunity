from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from django.urls import reverse

from beaunity.category.models import Category
from beaunity.category.views import CategoryOverviewView
from beaunity.common.mixins import UserModel

UserModel = get_user_model()


class TestCategoryOverviewView(TestCase):
    def setUp(self):
        Group.objects.get_or_create(name='User')
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='test123!A'
        )

        self.test_image = SimpleUploadedFile(
            name='test.gif',
            content=(
                b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
                b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
                b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01'
                b'\x00;'
            ),
            content_type='image/gif'
        )

        self.category1 = Category.objects.create(
            title='Skin care',
            description='Skin care description',
            image=self.test_image,
            created_by=self.user,
        )
        self.category2 = Category.objects.create(
            title='Morning Routine',
            description='Morning Routine description',
            image=self.test_image,
            created_by=self.user,
        )
        self.category3 = Category.objects.create(
            title='Trends',
            description='Trends description',
            image=self.test_image,
            created_by=self.user,
        )
        self.factory = RequestFactory()

    def test_queryset_with_params(self):
       request = self.factory.get(reverse('category-overview') + '?query=skin')
       view = CategoryOverviewView()

       view.request = request
       queryset = view.get_queryset()

       self.assertIn(self.category1, queryset)
       self.assertNotIn(self.category2, queryset)

    def test_queryset_without_params(self):
        request = self.factory.get(reverse('category-overview'))

        view = CategoryOverviewView()
        view.request = request
        queryset = view.get_queryset()

        self.assertIn(self.category1, queryset)
        self.assertIn(self.category2, queryset)
        self.assertIn(self.category3, queryset)
        self.assertTrue(len(queryset) == 3)