from django import forms
from beaunity.event.models import Event
from ckeditor.widgets import CKEditorWidget
import bleach
from cloudinary.forms import CloudinaryFileField
from django.forms import ClearableFileInput
from beaunity.category.models import Category

from beaunity.common.validators import CloudinaryExtensionandSizeValidator


CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
    )
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Your name:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        ),
    )
    email = forms.EmailField(
        label='Your Email:',
        widget=forms.EmailInput(
            attrs={
                'class': CLASS
            }
        )
    )
    subject = forms.CharField(
        max_length=100,
        label='Subject:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        )
    )
    content = forms.CharField(
        max_length=1000,
        label='Content:',
        widget=forms.Textarea(
            attrs={
                'class': CLASS
            }
        )
    )


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
            'folder': 'event_images',
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
        raw = self.cleaned_data['details']
        plain_text = bleach.clean(raw, tags=[], strip=True)
        if len(plain_text.strip()) < 100:
            raise forms.ValidationError("Description must be at least 100 characters (excluding formatting).")
        return raw

    def clean_poster_image(self):
        poster_image = self.cleaned_data['poster_image']
        validator = CloudinaryExtensionandSizeValidator()  # create instance
        validator(poster_image)
        return poster_image

    # def clean(self):
    #     cleaned_data = super().clean()
    #     online = cleaned_data.get('is_online')
    #     location = cleaned_data.get('location')
    #     meeting_link = cleaned_data.get('meeting_link')
    #     if not online and not location:
    #         self.add_error('location', 'Location is required if the event is not online.')
    #
    #     if online and not meeting_link:
    #         self.add_error('meeting_link', 'Meeting link is required if the event is online.')
    #     return cleaned_data
