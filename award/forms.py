from django import forms
from .models import Project,Profile,Review

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','view_grade']
class ProfileForm(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user']
class GradeForm(forms.ModelForm):
     class Meta:
         model= Review
         exclude = ['user','project','total','avg']