from django.test import TestCase
from .models import Project,Profile,Review
# Create your tests here.

class ProjectTestClass(TestCase):
       def setUp(self):
          self.profile=Profile(id=1,photo='yuly',bio='full-stack',phone_number=6789557608)
          self.project=Project(id=1,image='insta-G',title='instagram',description="nice images")
          self.review=Review(id=1,design=2,usability=2,content=2,total=0,avg=3,comment='NICE')


       def tearDown(self):
           Profile.objects.all().delete()
           Project.objects.all().delete()
           Review.objects.all().delete()

       def test_save_project(self):
         self.project.save_project()
         projects = Project.objects.all()
         self.assertTrue(len(projects) > 0)   

       def test_delete_project(self):
           self.project.save_project()
           self.project.delete_project()
           projects = Project.objects.all()
           self.assertTrue(len(projects) == 0) 

       def test_update_description(self):
           self.project.save_project()
           description='NICE'
           self.project.update_description(description)
           self.assertTrue( self.project.description == description) 

class ProfileTestClass(TestCase):
    def setUp(self):
        self.image= Profile(photo = 'yuly', bio ='full-stack',phone_number = '07854222',username='yuly')
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))
    def test_save_method(self):
        self.image.save_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) > 0)
    def test_delete(self):
        self.image= Profile(photo = 'yuly', bio ='image',phone_number = '07854222',username='yuly')
        self.image.save_profile()
        image = Profile.objects.filter(photo = 'yuly').first()
        delete = Profile.objects.filter(id = image.id).delete()
        images = Profile.objects.all()
        self.assertTrue(len(images) == 0)