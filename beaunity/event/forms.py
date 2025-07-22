from django import forms

from beaunity.common.forms import ActivityBaseForm

from .models import Event
from .mixins import EventValidationMixin, PublicFieldMixin


class EventCreateForm(ActivityBaseForm, EventValidationMixin, PublicFieldMixin):
    class Meta(ActivityBaseForm.Meta):
        model = Event


class EventEditForm(ActivityBaseForm, EventValidationMixin, PublicFieldMixin):
    class Meta(ActivityBaseForm.Meta):
        model = Event


class EventDeleteForm(ActivityBaseForm, PublicFieldMixin):
    class Meta(ActivityBaseForm.Meta):
        model = Event

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("categories", None)
        self.fields.pop("poster_image", None)
        for field_name in self.fields.keys():
            self.fields[field_name].disabled = True


