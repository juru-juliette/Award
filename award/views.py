from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='Awards'
    return render(request,'AW/home.html',{'title':title })

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            
            image.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'AW/post.html', {"form": form})