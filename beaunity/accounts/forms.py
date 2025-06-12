from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


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
    pass
