from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Project,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='Awards'
    post=Project.objects.all()
    profile = Profile.objects.all()
    return render(request,'AW/home.html',{'title':title ,'post':post,'profile':profile})

@login_required(login_url='/accounts/login/')
def profile(request):
     current_user = request.user
     if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()

        return redirect('edit_profile')

     else:
        form = ProfileForm()
     return render(request, 'AW/profile.html', {"form": form})
@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    picture = Profile.objects.filter(user= current_user).first()
    return render(request, 'AW/edit_profile.html', { "picture":picture})

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

        return render(request, 'AW/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'AW/search.html',{"message":message})
