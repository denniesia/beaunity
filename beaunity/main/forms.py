from django import forms

CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Your name:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        ),
    )
    email = forms.EmailField(
        label='Your Email:',
        widget=forms.EmailInput(
            attrs={
                'class': CLASS
            }
        )
    )
    subject = forms.CharField(
        max_length=100,
        label='Subject:',
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        )
    )
    content = forms.CharField(
        max_length=1000,
        label='Content:',
        widget=forms.Textarea(
            attrs={
                'class': CLASS
            }
        )
    )
