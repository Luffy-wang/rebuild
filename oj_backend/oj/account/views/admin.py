from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
@api_view(["GET","POST"])
def register(request):
    if not request.user.is_anonymous:
        return HttpResponse("login success")
    else:       
        name=request.data["name"]
        password=request.data["password"]
        user=User.objects.create_user(name,password=password)
        return HttpResponse(request,"account/logined.html")

def mylogin(request):
    name=request.POST["name"]
    password=request.POST["password"]
    user=authenticate(request,username=name,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect("index")
    
    return HttpResponse("ligin error")#todo

def index(request):
    return render(request,"account/index.html")#todo
def my_logut(request):
    logout(request)
    return HttpResponse("logout success")
    
def mylogin_index(request):
    return render(request,"account/ligined.html")

def get(request):
    return render(request,"account/register.html")