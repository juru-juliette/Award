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
     design= forms.IntegerField()
     usability= forms.IntegerField()
     content= forms.IntegerField()
     class Meta:
         model= Review
         exclude = ['user','project','total','avg']