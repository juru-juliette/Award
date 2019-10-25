from django import forms
from .models import Project
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']