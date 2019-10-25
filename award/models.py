from django.db import models
from django.contrib.auth.models import User
import datetime as dt 
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    photo=models.ImageField(upload_to='pic/')
    bio=models.TextField()
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    email = models.EmailField(max_length=100)
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()
    @classmethod
    def search_by_username(cls,search_term):
       users=cls.objects.filter(username__username__icontains=search_term)
       return users
class Project(models.Model):
     title=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'pic/')
     description=HTMLField()
     pub_date = models.DateTimeField(auto_now_add=True)
     profile=models.ForeignKey(Profile, null=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
     def save_project(self):
         self.save()

     def delete_project(self):
       self.delete()
       
     def update_description(self,des):
         self.description=des
         self.save() 
class Review(models.Model):
     design=models.CharField(max_length=100)
     usability=models.CharField(max_length=100)
     content=HTMLField()
     profile=models.ForeignKey(Profile, null=True)
     project=models.ForeignKey(Project, null=True)
