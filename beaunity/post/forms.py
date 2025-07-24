from django import forms

from beaunity.category.models import Category

from .models import Post

CLASS = "w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400"


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "banner", "title",
            "content", "category"
        ]

    category = forms.ModelChoiceField(
        label="Category:",
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                "class": CLASS
            }
        ),
        help_text="Once the post is approved the category cannot be changed."
    )

    banner = forms.URLField(
        label="Banner URL:",
        required=False,
        widget=forms.URLInput(
            attrs={
                "class": CLASS,
                "placeholder": "Please provide a URL link"
            }
        ),
    )
    title = forms.CharField(
        label="Title:",
        widget=forms.TextInput(
            attrs={
                "class": CLASS,
            }
        ),
    )
    content = forms.CharField(
        label="Content:",
        widget=forms.Textarea(
            attrs={
                "class": CLASS,
                "rows": 4,
            }
        ),
    )


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].disabled = True
        self.fields["category"].required = False


class AdminPostEditForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].disabled = True
        self.fields["content"].disabled = True
        self.fields["banner"].disabled = True
