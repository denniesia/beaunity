from django import forms
from .models import Event
from beaunity.category.models import Category
from cloudinary.forms import CloudinaryFileField
from django.forms import ClearableFileInput

CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'

class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['poster_image',
                  'title', 'details',
                  'is_online','city', 'location',
                  'meeting_link', 'start_time',
                  'end_time', 'categories']

    poster_image = CloudinaryFileField(
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
        widget=forms.Textarea(
            attrs={
                'class': CLASS,
            }
        ),
        help_text='Please enter at least 100 characters describing the event.',
    )
    is_online = forms.BooleanField(
        label='Online event:  ',
        widget=forms.CheckboxInput(
        )
    )
    city = forms.CharField(
        label='City:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS,
            }
        )
    )
    location = forms.CharField(
        label='Location:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS,
            },
        ),
        help_text='Please enter the street, the city and the country, where the event will take place.',

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
        help_text="Select one or more categories that apply to this event."
    )

class EventEditForm(EventBaseForm):
    pass
