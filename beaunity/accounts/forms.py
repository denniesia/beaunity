from cloudinary.forms import CloudinaryFileField
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ClearableFileInput

from beaunity.accounts.models.choices import SkinTypeChoices
from beaunity.common.validators import CloudinaryExtensionandSizeValidator

from .models import Profile

UserModel = get_user_model()
CLASS = "w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400"


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = (
            "username",
            "email",
        )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":
                    CLASS
            }
        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs=
            {
                "class": CLASS
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        help_text='Use at least 8 characters. Combine letters (A-Z, a-z), numbers (0-9), and symbols (!@#...). '
                  'Don’t use your name, email, or simple words like "password".',
        widget=forms.PasswordInput(
            attrs=
            {
                "class": CLASS
            }
        ),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs=
            {
                "class": CLASS
            }
        ),
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if UserModel.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email


class AppUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or email",
        widget=forms.TextInput(
            attrs={
                "class": CLASS,
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": CLASS,
            }
        )
    )


class AppUserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ("email",)

    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": CLASS,
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not email:
            return self.instance.email

        if UserModel.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This email is already in use.")

        return email

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)

    profile_pic = CloudinaryFileField(
        label="Profile Picture:",
        required=False,
        help_text="Allowed profile pic extentions are -.jpg, .jpeg, .png, .gif, .pdf,.mp4. Allowed size is 5MB.",
        options={
            "folder": "profile_pics",  # optional: where to store images in your Cloudinary account
            "use_filename": True,
            "unique_filename": True,
        },
        widget=ClearableFileInput(
            attrs={
                "class": CLASS,
            }
        ),
    )
    first_name = forms.CharField(
        required=False,
        label="First Name:",
        widget=forms.TextInput(
            attrs={
                "class": CLASS,
            }
        ),
    )
    last_name = forms.CharField(
        required=False,
        label="Last Name:",
        widget=forms.TextInput(
            attrs={
                "class": CLASS
            }
        ),
    )
    date_of_birth = forms.DateField(
        required=False,
        label="Date of Birth:",
        widget=forms.DateInput(
            attrs={
                "class": CLASS,
                "type": "date"
            },
            format="%Y-%m-%d"
        ),
        input_formats=["%Y-%m-%d"],
    )
    bio = forms.CharField(
        required=False,
        label="Bio:",
        widget=forms.Textarea(
            attrs={
                "class": CLASS,
                "rows": 4,
            }
        ),
    )
    skin_type = forms.CharField(
        required=False,
        label="Skin Type:",
        widget=forms.Select(
            attrs={
                "class": CLASS,
            },
            choices=SkinTypeChoices,
        ),
    )
    location = forms.CharField(
        required=False,
        label="Location:",
        widget=forms.TextInput(
            attrs={
                "class": CLASS,
            }
        ),
    )

    def clean_profile_pic(self):
        profile_pic = self.cleaned_data["profile_pic"]
        if profile_pic:
            CloudinaryExtensionandSizeValidator()(profile_pic)
        return profile_pic


class ProfileEditForm(ProfileBaseForm):
    pass
