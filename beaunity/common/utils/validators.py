from django.core.exceptions import ValidationError
import os

def cloudinary_file_validator(file):
    max_size_mb = 5
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.mp4']

    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"File size must be under {max_size_mb} MB.")

    extension = os.path.splitext(file.name)[1].lower()
    if extension not in allowed_extensions:
        raise ValidationError(f"Unsupported file type: {extension}.")