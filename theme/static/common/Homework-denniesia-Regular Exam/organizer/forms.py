from django import forms
from .models import Organizer


class OrganizerBaseForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ('company_name', 'phone_number','secret_key')

    company_name = forms.CharField(
        label='Company Name',
        help_text="*Allowed names contain letters, digits, spaces, and hyphens." ,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your company name...',
            }
        ),
    )
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Enter a valid phone number (digits only)...",
            }
        ),
        error_messages={
            'unique': "That phone number is already in use!",
        }
    )



class OrganizerCreateForm(OrganizerBaseForm):
    class Meta(OrganizerBaseForm.Meta):
        fields = ('company_name', 'phone_number', 'secret_key')

    secret_key = forms.CharField(
        label='Secret Key',
        help_text="*Pick a combination of 4 unique digits.",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Enter a secret key like <1234>...",
            }
        )
    )

class OrganizerEditForm(OrganizerBaseForm):
    class Meta:
        model = Organizer
        fields = ('company_name', 'phone_number', 'website')

        help_texts = {
            'company_name': '*Allowed names contain letters, digits, spaces, and hyphens.',
        }

    website = forms.URLField(
        label='Website:',
        required=False,
    )
