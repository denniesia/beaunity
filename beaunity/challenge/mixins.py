from django import forms
from .choices import DifficultyLevel


class ChallengeValidationMixin:
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data is None:
            cleaned_data = self.cleaned_data  # fallback

        online = cleaned_data.get("is_online", '')
        location = cleaned_data.get("location", '')

        if not online and not location:
            self.add_error(
                "location", "Location is required if the event is not online."
            )

        return cleaned_data


class DifficultyFieldMixin(forms.Form):
    difficulty = forms.ChoiceField(
        choices=DifficultyLevel,
        label="Difficulty:",
        widget=forms.Select(
            attrs={
                "class": "w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400",
            }
        ),
    )