import os

from cloudinary.models import CloudinaryResource
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CloudinaryExtensionandSizeValidator:
    def __init__(self, max_size_mb=5):
        self.max_size_mb = max_size_mb

    @property
    def allowed_extensions(self):
        return [".jpg", ".jpeg", ".png", ".gif", ".pdf", ".mp4"]

    def __call__(self, file):
        if isinstance(file, CloudinaryResource):
            return

        if file.size > self.max_size_mb * 1024 * 1024:
            raise ValidationError(f"File size must be under {self.max_size_mb} MB.")

        extension = os.path.splitext(file.name)[1].lower()

        if extension not in self.allowed_extensions:
            raise ValidationError(f"Unsupported file type: {extension}.")
