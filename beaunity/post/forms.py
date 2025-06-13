from django import forms
from .models import Post
from beaunity.category.models import Category

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostEditForm(PostBaseForm):
    CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'
    class Meta(PostBaseForm.Meta):
        fields = ['banner', 'title', 'content', 'category']

    banner = forms.URLField(
        widget=forms.URLInput(
            attrs={
                'class': CLASS
            }
        ),
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        ),
    )
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': CLASS
            }
        ),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': CLASS
        })
    )

