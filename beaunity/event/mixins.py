from django import forms


class EventValidationMixin:
    def clean(self):
        cleaned_data = super().clean()
        online = cleaned_data.get("is_online")
        location = cleaned_data.get("location")
        meeting_link = cleaned_data.get("meeting_link")

        if not online and not location:
            self.add_error(
                "location", "Location is required if the event is not online."
            )

        if online and not meeting_link:
            self.add_error(
                "meeting_link", "Meeting link is required if the event is online."
            )
        return cleaned_data

class PublicFieldMixin(forms.Form):
    is_public = forms.BooleanField(
        label="Public event:",
        required=False,
        widget=forms.CheckboxInput(),
        initial=False,
    )