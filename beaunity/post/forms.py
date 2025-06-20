from django import forms
from .models import Post
from beaunity.category.models import Category

CLASS = 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['banner', 'title', 'content', ]

    banner = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                'class': CLASS,
                'placeholder': 'Please provide a URL link'
            }
        ),
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': CLASS,
            }
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': CLASS,
                'rows': 4,
            }

        ),
    )

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = PostBaseForm.Meta.fields + ['category']

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': CLASS
        })
    )


class PostEditForm(PostBaseForm):
    pass

class AdminPostEditForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['content'].disabled = True

    class Meta(PostBaseForm.Meta):
        fields = ['category']

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': CLASS
        })
    )

