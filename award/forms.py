from django import forms
from .models import Project,Profile
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']
class ProfileForm(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user']