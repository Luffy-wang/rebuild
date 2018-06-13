from account.models import User,User_type
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from django.contrib import admin
#from ..serializer import MyclassSerializer,ShowClassSerializer
from django.forms.models import model_to_dict
from utils.api.utils import MyBaseView
from myclass.models import Myclass
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View
import os,time
import xlrd
from django.core.cache import cache
from django_redis import get_redis_connection
from ..tasks import butch_create
from ..serializer import UserSerialzier

class LoginIndex(MyBaseView):
    def get(self,request):
        return render(request,"account/login.html")


class UserAbout(MyBaseView):  #登录，登出
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        logout(request)
        return JsonResponse({'data':1})
    @method_decorator(ensure_csrf_cookie)
    def post(self,request):
        data=request.data
        user_id=data.get("userid")
        #return HttpResponse(user_id)
        password=data.get("password")
        user_type=User.objects.values('user_type').filter(user_id=user_id).first()
        #user_type=model_to_dict(user_type)
        #user_type=User.objects.get
        user=authenticate(request,user_id=user_id,password=password)
        #return HttpResponse(user)
        if user is not None:
            if request.user.is_authenticated:
                return JsonResponse({'data':2,"msg":"已登录，请不要重复登录"},safe=False)#already login
            else:
                login(request,user)
                return JsonResponse({"data":1,"msg":"登录成功",'name':request.user.user_name},safe=False)
        else:
            return JsonResponse({"data":0,"msg":"验证失败"},safe=False)

    def put(self,request):
        data=request.data
        user_id=data.get('user_id')
        new_password=data.get('newpwd')
        old_password=data.get('oldpwd')                             
        user_type=request.user
        if User.is_student(user_type):
            user_id=request.user.user_id
        user=authenticate(request,user_id=user_id,password=int(old_password))
        u=User.objects.get(user_id=user_id)
        if user:
            u.set_password(int(new_password))
            u.save()
            return JsonResponse({'data':1,'msg':'修改成功'})
        else:
            return JsonResponse({'data':0,'msg':'验证失败'})



class ModifyUser(MyBaseView):
    def get(self,request):
        try:
            user_type=request.user.user_type
            return JsonResponse({'data':1,'user_type':user_type})
        except:
            return JsonResponse({'data':0,'user_type':'游客'})
    def post(self,request):
        user_type=request.data.get('type')
        user_id=request.data.get('user_id')
        try:
            User.objects.filter(user_id=user_id).update(user_type=user_type)
            return JsonResponse({'data':1,"msg":'修改成功'},safe=False)
        except:
            return JsonResponse({'data':0,"msg":'修改失败'},safe=False)

class ShowUser(MyBaseView):
    def get(self,request):
        page=request.data.get("page")
        user=User.objects.all()
        #return HttpResponse(user)
        
        data=super(ShowUser,self).paginator_data(user,page)
        serializer=UserSerialzier(data,many=True)
        return JsonResponse(serializer.data,safe=False)


class UserRegister(View):#MyBaseView):
    con=get_redis_connection("default")

    
    @method_decorator(ensure_csrf_cookie)
    def post(self,request):
        file=request.FILES["userinformation"]
        user_excel=os.path.join("/tmp","user.excel")
        with open(user_excel,"wb") as f:
            for chunk in file:
                f.write(chunk)
        data=xlrd.open_workbook("/tmp/user.excel")
        table=data.sheets()[0]
        self.nrows=table.nrows
        ncols=table.ncols
        for rows in range(self.nrows):
            cr=table.row_values(rows)
            data_id=cr[0]
            data_name=cr[1]
            try:
                butch_create.delay(user_id=data_id,user_name=data_name,password=123456)
            except:
                return JsonResponse({'data':0,'msg':'上传失败'})
        return JsonResponse({'data':1,'msg':'上传成功'})
            