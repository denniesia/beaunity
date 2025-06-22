from django import forms
from .models import Event
from django.utils import timezone
from datetime import datetime

from common.mixins import ReadOnlyMixin

class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer']

    slogan = forms.CharField(
        label='Slogan:',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Provide an appealing text...',
            }
        )
    )
    location = forms.CharField(
        label='Location:',
    )
    start_time = forms.DateTimeField(
        label='Event Date/Time:',
        initial=timezone.now,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local'
            },
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    available_tickets = forms.IntegerField(
        label='Available Tickets:',

    )
    key_features = forms.CharField(
        label='Event Key Feautures:',
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Provide important event details...',
            }
        )
    )
    banner_url = forms.URLField(
        label='Event Banner URL:',
        required=False,
        widget=forms.URLInput(
            attrs={
                'placeholder': "An optional banner image URL...",
            }
        )
    )

class EventCreateForm(EventBaseForm):
    pass


class EventEditForm(EventBaseForm):
    pass

class EventDeleteForm(ReadOnlyMixin,EventBaseForm):
    readonly_fields = ['slogan', 'location', 'start_time', 'available_tickets', 'key_features', 'banner_url']
