import bleach
from ckeditor.widgets import CKEditorWidget
from cloudinary.forms import CloudinaryFileField
from django import forms
from django.forms import ClearableFileInput

from beaunity.category.models import Category
from beaunity.common.validators import CloudinaryExtensionandSizeValidator
from beaunity.event.models import Event

CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'


class ActivityBaseForm(forms.ModelForm):
    CLASS = CLASS
    class Meta:
        fields = ['poster_image',
                  'title', 'details',
                  'is_online',
                  'city', 'location',
                  'meeting_link', 'start_time',
                  'end_time', 'categories']

    poster_image = CloudinaryFileField(
        label='Poster Image:',
        help_text='Allowed poster image extentions are -.jpg, .jpeg, .png, .gif, .pdf, .mp4. Allowed size is 5MB.',
        options={
            'folder': 'activity_images',
            'use_filename': True,
            'unique_filename': True,
        },
        widget=ClearableFileInput(
            attrs={
                'class': CLASS,
            }
        )
    )

    title = forms.CharField(
        label='Title:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS,
            }
        )
    )

    details = forms.CharField(
        label='Details:',
        widget=CKEditorWidget(
            attrs={
                'class': CLASS,
                'rows': 11,
            }
        ),
        help_text='Please enter at least 100 characters describing the details.',
    )

    is_online = forms.BooleanField(
        label='Online:',
        required=False,
        widget=forms.CheckboxInput()
    )

    city = forms.CharField(
        label='City:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': CLASS,
            }
        )
    )

    location = forms.CharField(
        label='Location:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': CLASS,
            },
        ),
        help_text='Please enter the street, the city and the country, where the it will take place.',
    )

    meeting_link = forms.URLField(
        label='Meeting Link:',
        required=False,
        widget=forms.URLInput(
            attrs={
                'class': CLASS,
            }
        )
    )

    start_time = forms.DateTimeField(
        label='Start Time:',
        widget=forms.DateTimeInput(
            attrs={
                'class': CLASS,
                'type': 'datetime-local',
            },
            format='%Y-%m-%dT%H:%M',
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    end_time = forms.DateTimeField(
        label='End Time:',
        widget=forms.DateTimeInput(
            attrs={
                'class': CLASS,
                'type': 'datetime-local',
            },
            format='%Y-%m-%dT%H:%M',
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    categories = forms.ModelMultipleChoiceField(
        label='Categories:',
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'h-fit border border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400 p-2 space-y-2'
            }
        ),
        help_text="Select one or more categories."
    )

    def clean_details(self):
        ALLOWED_TAGS = ['b', 'i', 'u', 'a', 'p', 'ul', 'li', 'strong', 'em', 'br']
        ALLOWED_ATTRIBUTES = {
            'a': ['href', 'title'],
        }

        raw = self.cleaned_data['details']
        plain_text = bleach.clean(raw, tags=[], strip=True)

        if len(plain_text.strip()) < 100:
            raise forms.ValidationError("Description must be at least 100 characters (excluding formatting).")

        return bleach.clean(
            raw,
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRIBUTES,
            strip=True
        )

    def clean_poster_image(self):
        poster_image = self.cleaned_data['poster_image']
        validator = CloudinaryExtensionandSizeValidator()  # create instance
        validator(poster_image)
        return poster_image



class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Search posts...",
            "class": "w-full px-3 py-2 border border-pink-300 rounded-full text-sm text-gray-700 placeholder-pink-400 focus:outline-none focus:ring-2 focus:ring-pink-300 focus:border-pink-400 transition duration-200"
        })
    )