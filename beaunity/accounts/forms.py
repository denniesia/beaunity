from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from beaunity.accounts.models.choices import SkinTypeChoices
from cloudinary.forms import CloudinaryFileField
from django.forms import ClearableFileInput

UserModel = get_user_model()
CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'

class AppUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email',)

    username = forms.CharField(
    widget=forms.TextInput(
        attrs={
            'class': CLASS
        }
    ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': CLASS
            }
        ),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': CLASS
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': CLASS
            }
        )
    )

class AppUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username or email',
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':CLASS
            }
        )
    )

'''Profile Forms'''

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class ProfileEditForm(ProfileBaseForm):
    profile_pic =  CloudinaryFileField(
        label='Profile Picture',
        required=False,
        options={
            'folder': 'profile_pics',  # optional: where to store images in your Cloudinary account
            'use_filename': True,
            'unique_filename': True,
        },
        widget=ClearableFileInput(
            attrs={
                'class': CLASS
            }
        )
    )
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': CLASS,

            }
        )
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        )
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': CLASS,
                'type': 'date'
            },
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d']
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': CLASS,
                'rows': 4,
            }
        )
    )
    skin_type = forms.CharField(
        required=False,
        widget=forms.Select(
            attrs={
                'class': CLASS,
            },
            choices = SkinTypeChoices
        )
    )
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': CLASS,
            }
        )
    )
    joined_events = forms.CharField(
        required=False,
    )

class AppUserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': CLASS
            }
        )
    )

