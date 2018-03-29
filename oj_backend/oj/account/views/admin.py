from account.models import User,Myclass,User_type
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import admin
from ..serializer import MyclassSerializer,ShowClassSerializer
from django.forms.models import model_to_dict

#admin.site.register(User,UserAdmin)

#from corsheaders.defaults import default_headers
@api_view(["GET","POST"])
def register(request):
    if  request.user.is_authenticated:   #to verify 
        return HttpResponse("login success")
    else:
        data=json.loads(request.body.decode("utf-8"))
        user_id=data["user_id"]       
        name=data["name"]
        password=data["password"]
        user=User.objects.create_user(user_id=user_id,user_name=name,password=password)
        return HttpResponse("SUCCESS")
@csrf_exempt   #todo delete

def mylogin(request):
    # if request.method=="OPTIONS":
    #     response=HttpResponse()
        
    #     response["Access-Control-Allow-Origin"]="*"
    #     response["Access-Control-Allow-Methods"]="POST,GET,OPTIONS"
    #     response["Access-Control-Max-Age"]="1000"
    #     response["Access-Control-Allow-Headers"]="*"
        
    #     return response
    #CORS_ALLOW_HEADERS=default_headers+("aaa")
    data=json.loads(request.body.decode("UTF-8"))
    user_id=data["user_id"]
    password=data["password"]
    user=authenticate(request,user_id=user_id,password=password)
    
    if user is not None:
        if request.user.is_authenticated:
            return JsonResponse({'data':0},safe=False)#already login
        else:
            login(request,user)
            return JsonResponse({"data":1,"user_id":user_id},safe=False)
    else:
        return JsonResponse({"data":0},safe=False)

@csrf_exempt
def mylogut(request):
    logout(request)
    return HttpResponse("logout success")

#if admin want to use this function.it should give the teacher id
@csrf_exempt
@login_required
def create_class(request):
    data=json.loads(request.body.decode("utf-8"))
    class_name=data["class_name"]
    user_id=data["user_id"]
   
    u=User.objects.get(user_id=user_id)
    if User.is_teacher(u):
        myclass=Myclass.objects.create(class_name=class_name,class_admin=u,class_member=u,is_activity=True)
        return JsonResponse({"data":1})
    elif User.is_admin(u):
        return HttpResponse("error action")
    else:
        c=Myclass.objects.filter(class_member=u)
        if c:
            return JsonResponse({"data":0})
        else:
            myclass=Myclass.objects.create(class_name=class_name,class_member=u)
            return JsonResponse({"data":1})
    
#required admin
@csrf_exempt
@login_required
def modify_user_type_to_teacher(request):
    data=json.loads(request.body.decode("utf-8"))
    user_id=data["teacher_id"]
    admin_id=data['user']
    a=User.objects.get(user_id=admin_id)
    if(User.is_admin(a)):
        class_member_id=User.objects.get(user_id=user_id)
        
        if not get_object_or_404(Myclass,class_member_id=class_member_id):
            return JsonResponse({'data':0},safe=False)#already in class
        else:
            User.objects.filter(user_id=user_id).update(user_type=User_type.TEACHER)
        return JsonResponse({'data':1},safe=False)
    else:
        return JsonResponse({'data':0},safe=False)
#get function 
# login required 
# teacher required?
@csrf_exempt
@login_required
def show_class_member_or_class(request):
    data=json.loads(request.body.decode("utf-8"))
    
    user_id=data["user_id"]
    u=Myclass.objects.get(class_member=user_id)
    if u.is_activity:
        u=model_to_dict(u)
        class_member=Myclass.objects.filter(class_name=u["class_name"])
        serializer=MyclassSerializer(class_member,many=True)
        
        return JsonResponse(serializer.data,safe=False)
    else:
        class_name=Myclass.objects.values("class_name").distinct()
        #serializer=MyclassSerializer(class_name,many=True)
        serializer=ShowClassSerializer(class_name,many=True)
        
        return JsonResponse(serializer.data,safe=False)
#teacher required
@csrf_exempt
def not_join_the_class(request):
    user=Myclass.objects.filter(is_activity=False)
    serializer=MyclassSerializer(user,many=True)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
@login_required
def join_the_class(request):
    data=json.loads(request.body.decode("utf-8"))
    student_id=data["student_id"]
    Myclass.objects.filter(class_member=student_id).update(is_activity=True)
    return JsonResponse({"data":1})
@csrf_exempt
def showclassname(request):
    data=json.loads(request.body.decode('utf-8'))
    student_id=data['student_id']
    class_name=Myclass.objects.get(class_member=student_id)
    class_name=model_to_dict(class_name)
    return JsonResponse({'data':1,'class_name':class_name['class_name']},safe=False)
