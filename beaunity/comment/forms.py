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
                    'placeholder': 'Comments must be at least 5 characters long...',
                    'rows': 3,
                }
            )
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if len(content) < 5:
            raise forms.ValidationError('Comments must be at least 5 characters.')
        return content

class CommentCreateForm(CommentBaseForm):
    pass

class CommentEditForm(CommentBaseForm):
    pass
