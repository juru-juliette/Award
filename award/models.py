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
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone_number=models.IntegerField(null=True)
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

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
class Project(models.Model):
     title=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'pic/')
     description=HTMLField()
     pub_date = models.DateTimeField(auto_now_add=True)
     profile=models.ForeignKey(Profile, null=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     view_grade=models.IntegerField(null=True)
     def save_project(self):
         self.save()

     def delete_project(self):
       self.delete()
       
     def update_description(self,des):
         self.description=des
         self.save() 
class Review(models.Model):
     design=models.IntegerField()
     usability=models.IntegerField()
     content=models.IntegerField()
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

