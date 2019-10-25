from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect

# Create your views here.
# @login_required(login_url='/accounts/login/')
def home(request):
    title='Awards'
    return render(request,'AW/home.html',{'title':title })