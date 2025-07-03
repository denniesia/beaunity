from django import forms
from .models import Category
from cloudinary.forms import CloudinaryFileField
from django.forms import ClearableFileInput
from beaunity.common.utils.validators import cloudinary_file_validator

CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'
class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['created_by',]
        error_messages = {
            'title': {
                'unique': 'Such title already exists.'
            }
        }

    image = CloudinaryFileField(
        label='Image',
        help_text='Allowed image extentions are -.jpg, .jpeg, .png, .gif, .pdf, .mp4. Allowed size is 5MB.',
        options={
            'folder': 'category_images',  # optional: where to store images in your Cloudinary account
            'use_filename': True,
            'unique_filename': True,
        },

        widget=ClearableFileInput(
            attrs={
                'class': CLASS
            }
        )
    )

    title = forms.CharField(
        label='Title:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        ),

    )
    description = forms.CharField(
        label='Description:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        ),
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        return title[0].upper() + title[1:] if title else title

    def clean_description(self):
        description = self.cleaned_data['description']
        return description[0].upper() + description[1:] if description else description

    def clean_image(self):
        image = self.cleaned_data['image']
        cloudinary_file_validator(profile_pic)
        return image


class CategoryCreateForm(CategoryBaseForm):
    pass

class CategoryEditForm(CategoryBaseForm):
    pass

class CategoryDeleteForm(CategoryBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,

    )
