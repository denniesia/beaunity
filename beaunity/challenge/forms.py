from django import forms
from beaunity.common.forms import ActivityBaseForm
from .choices import DifficultyLevel
from .models import Challenge

class ChallengeCreateForm(ActivityBaseForm):
    class Meta(ActivityBaseForm.Meta):
        model = Challenge

    difficulty = forms.ChoiceField(
        choices=DifficultyLevel,
        label="Difficulty:",
        widget=forms.Select(
            attrs={
                'class': 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400',
            }
        )

    )