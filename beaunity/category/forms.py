from django import forms
from .models import Category

class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['created_by',]

    title = forms.CharField(
        label='Title:',
        widget=forms.TextInput(
            attrs={
                'class': 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'
            }
        ),
    )
    description = forms.CharField(
        label='Description:',
        widget=forms.TextInput(
            attrs={
                'class': 'w-full px-4 py-2 border border-pink-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-400'
            }
        ),
    )

class CategoryCreateForm(CategoryBaseForm):
    pass

class CategoryEditForm(CategoryBaseForm):
    pass

class CategoryDeleteForm(CategoryBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,

    )
