from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Project,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='Awards'
    post=Project.objects.all()
    return render(request,'AW/home.html',{'title':title ,'post':post})
@login_required(login_url='/accounts/login/')
def profile(request,id):
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     projects=Project.objects.filter(user=user)
    
     return render(request, 'AW/profile.html',{"user":user,"profile": profile,'projects':projects})
     
@login_required(login_url='/accounts/login/')
def edit_profile(request,edit):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)
    
   
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['photo']
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.phone_number = form.cleaned_data['phone_number']
            profile.user=current_user
            
            profile.save()
        return redirect('home')

    else:
        form = Profileform()
    return render(request, 'AW/edit_profile.html', {"form": form , 'user':current_user})

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