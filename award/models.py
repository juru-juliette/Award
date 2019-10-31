from django.db import models
from django.contrib.auth.models import User
import datetime as dt 
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    photo=models.ImageField(upload_to='pic/')
    bio=models.TextField()
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    phone_number=models.CharField(max_length=50)
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(username=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()
class Project(models.Model):
     title=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'pic/')
     description=HTMLField()
     link= models.CharField(max_length=200)
     profile=models.ForeignKey(Profile,null=True)
     view_grade=models.IntegerField(null=True)
     def save_project(self):
         self.save()

     def delete_project(self):
       self.delete()
       
     def update_description(self,des):
         self.description=des
         self.save()
     @classmethod
     def search_project(cls,search_term):
       project=cls.objects.filter(title__icontains=search_term)
       return project 
class Review(models.Model):
     design=models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
     usability=models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
     content=models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     project=models.ForeignKey(Project)
     total=models.IntegerField()
     avg=models.IntegerField(null=True)
     comment=models.TextField(null=True)

     def save_review(self):
         self.save()
     def delete_review(self):
         self.delete()

     def update_comment(self,comment):
         self.comment=comment
         self.save()

