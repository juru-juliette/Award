from django import forms
from .models import Project,Profile,Review
from .choices import *

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','view_grade']
class ProfileForm(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user']
class Gradeform(forms.ModelForm):
     design= forms.ChoiceField(choices=VOTE_CHOICES)
     usability= forms.ChoiceField(choices=VOTE_CHOICES)
     content= forms.ChoiceField(choices=VOTE_CHOICES)
     class Meta:
         model= Review
         exclude = ['user','project','total','avg']