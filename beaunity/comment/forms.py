from django import forms
from .models import Comment

CLASS = "w-full text-sm border border-gray-300 rounded-md px-2 py-1 focus:outline-none focus:ring-1 focus:ring-pink-400 resize-none"

class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': CLASS,
                    'placeholder': 'Comments must be longer than 5 characters...',
                    'rows': 4,
                }
            )
        }


class CommentCreateForm(CommentBaseForm):
    pass
