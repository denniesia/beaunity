from django import forms
from .models import Category

class CategoryCreateForm(forms.ModelForm):
    model = Category