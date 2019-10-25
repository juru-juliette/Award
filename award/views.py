from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
# Create your views here.
# @login_required(login_url='/accounts/login/')
def home(request):
    title='Awards'
    return render(request,'home.html',{'title':title })