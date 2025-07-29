from django import forms

from beaunity.common.forms import ActivityBaseForm

from .models import Challenge
from .mixins import ChallengeValidationMixin, DifficultyFieldMixin

CLASS = "w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400"


class ChallengeCreateForm(DifficultyFieldMixin, ChallengeValidationMixin, ActivityBaseForm):
    class Meta(ActivityBaseForm.Meta):
        model = Challenge
        fields = ActivityBaseForm.Meta.fields + ['difficulty', ]


class ChallengeEditForm(DifficultyFieldMixin, ChallengeValidationMixin, ActivityBaseForm):
    class Meta(ActivityBaseForm.Meta):
        model = Challenge
        fields = ActivityBaseForm.Meta.fields + ['difficulty', ]


class ChallengeDeleteForm(ActivityBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("categories", None)
        self.fields.pop("poster_image", None)
        for field_name in self.fields.keys():
            self.fields[field_name].disabled = True

    class Meta(ActivityBaseForm.Meta):
        model = Challenge
