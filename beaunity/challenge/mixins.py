class ChallengeValidationMixin:
    def clean(self):
        cleaned_data = super().clean()
        online = cleaned_data.get("is_online")
        location = cleaned_data.get("location")

        if not online and not location:
            self.add_error(
                "location", "Location is required if the event is not online."
            )

        return cleaned_data
