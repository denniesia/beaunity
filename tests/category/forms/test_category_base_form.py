from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from beaunity.category.forms import CategoryBaseForm


class TestCategoryBaseForm(TestCase):
    def setUp(self):
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
        self.valid_data = {
            'title': 'Test Category',
            'description': 'Test Description',
        }

    def test__form_is_valid_expects_true(self):
        form = CategoryBaseForm(data=self.valid_data, files={'image': self.test_image})
        self.assertTrue(form.is_valid())

    def test__title_is_capitalized_expects_true(self):
        self.valid_data['title'] = 'test category'
        form = CategoryBaseForm(
            data=self.valid_data,
            files={'image': self.test_image}
        )

        self.assertTrue(form.is_valid())

        category = form.save(commit=False)

        self.assertEqual(
            category.title,
            self.valid_data['title'].capitalize(),
        )

    def test__description_is_capitalized_expect_true(self):
        self.valid_data['description'] = 'test description'
        form = CategoryBaseForm(
            data=self.valid_data,
            files={'image': self.test_image}
        )

        self.assertTrue(form.is_valid())

        category = form.save(commit=False)
        self.assertEqual(
            category.description,
            self.valid_data['description'].capitalize()
        )
