from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Project,Profile,Review
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm,GradeForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='Awards'
    post=Project.objects.all()
    profile = Profile.objects.all()
    grade= Review.objects.all()
    current_user=request.user
    return render(request,'AW/home.html',{'title':title ,'post':post,'profile':profile,'current_user':current_user,'grade':grade})

@login_required(login_url='/accounts/login/')
def profile(request,id):
   user_object = request.user
   current_user = Profile.objects.get(username__id=request.user.id)
   user = Profile.objects.get(username__id=id)
   projects = Project.objects.all()
   return render(request, "AW/profile.html", {"current_user":current_user,"projects":projects,"user":user,"user_object":user_object})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
   current_user=request.user
   user_edit = Profile.objects.get(username__id=current_user.id)
   if request.method =='POST':
       form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
       if form.is_valid():
           form.save()
           return redirect('profile')
   else:
       form=ProfileForm(instance=request.user.profile)
   return render(request,'AW/edit_profile.html',locals())

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'AW/post.html', {"form": form})
@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'AW/search.html',{"message":message,"project": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'AW/search.html',{"message":message})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url='/accounts/login/')
def grade_project(request,id):
     current_user=request.user
     project=Project.objects.get(id=id)
     if request.method == 'POST':
        form = GradeForm(request.POST, request.FILES)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.user = current_user
            grade.project=project
            grade.total=int(form.cleaned_data['design'])+int(form.cleaned_data['content'])+int(form.cleaned_data['usability'])
            grade.avg= int(grade.total)/3
            grade.save()
        return redirect('home')

     else:
        form = GradeForm()
     return render(request, 'AW/grade.html', {"form": form, 'proj':project})

    