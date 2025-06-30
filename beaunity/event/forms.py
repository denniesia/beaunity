from django import forms
from .models import Event
import re
from ckeditor.widgets import CKEditorWidget
from beaunity.category.models import Category
from cloudinary.forms import CloudinaryFileField
from django.forms import ClearableFileInput

CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'

class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['poster_image',
                  'title', 'details',
                  'is_online', 'is_public',
                  'city', 'location',
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
        widget=CKEditorWidget(
            attrs={
                'class': CLASS,
                'rows': 11,
            }
        ),
        help_text='Please enter at least 100 characters describing the event.',
    )
    is_online = forms.BooleanField(
        label='Online event:',
        required=False,
        widget=forms.CheckboxInput()
    )
    is_public = forms.BooleanField(
        label='Public event:',
        required=False,
        widget=forms.CheckboxInput(),
        initial=True
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

    def clean_details(self):
        raw = self.cleaned_data['details']
        plain_text = re.sub('<[^<]+?>', '', raw)
        if len(plain_text.strip()) < 100:
            raise forms.ValidationError("Description must be at least 100 characters (excluding formatting).")
        return raw

class EventCreateForm(EventBaseForm):
    pass


class EventEditForm(EventBaseForm):
    pass

class EventDeleteForm(EventBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('categories', None)
        self.fields.pop('poster_image', None)
        for field_name in self.fields.keys():
            self.fields[field_name].disabled = True


