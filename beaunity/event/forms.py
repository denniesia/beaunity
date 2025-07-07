from django import forms
from .models import Event
from beaunity.common.forms import ActivityBaseForm


class EventCreateForm(ActivityBaseForm):
    class Meta(ActivityBaseForm.Meta):
        model = Event

    is_public = forms.BooleanField(
        label='Public event:',
        required=False,
        widget=forms.CheckboxInput(),
        initial=True
    )
    def clean(self):
        cleaned_data = super().clean()
        online = cleaned_data.get('is_online')
        location = cleaned_data.get('location')
        meeting_link = cleaned_data.get('meeting_link')
        if not online and not location:
            self.add_error('location', 'Location is required if the event is not online.')

        if online and not meeting_link:
            self.add_error('meeting_link', 'Meeting link is required if the event is online.')
        return cleaned_data


class EventEditForm(ActivityBaseForm):
    class Meta(ActivityBaseForm.Meta):
        model = Event

    is_public = forms.BooleanField(
        label='Public event:',
        required=False,
        widget=forms.CheckboxInput(),
        initial=True
    )

class EventDeleteForm(ActivityBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('categories', None)
        self.fields.pop('poster_image', None)
        for field_name in self.fields.keys():
            self.fields[field_name].disabled = True

    class Meta(ActivityBaseForm.Meta):
        model = Event

    is_public = forms.BooleanField(
        label='Public event:',
        required=False,
        widget=forms.CheckboxInput(),
        initial=True
    )