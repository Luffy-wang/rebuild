from utils.api.utils import MyBaseView
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from account.models import User
from ..models import Myclass,MyClassIndex
from ..serializer import MyclassSerializer,ShowClassSerializer
from django.forms.models import model_to_dict
import json

class Mycclass(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        page=request.data.get('page')
        myclass=MyClassIndex.objects.all()
        data=super(Mycclass,self).paginator_data(myclass,page)
        serializer=ShowClassSerializer(data,many=True)
        return JsonResponse(serializer.data,safe=False)


    @method_decorator(ensure_csrf_cookie)
    def post(self,request):
        data=request.data               
        class_name=data.get("class_name")
        user_id=data.get('class_admin')
        try:
            u=User.objects.get(user_id=user_id)
        except:
            return JsonResponse({'data':0,'msg':'用户不存在'},safe=False)
        try:
            MyClassIndex.objects.create(class_name=class_name,class_admin=u)
            new_class_name=MyClassIndex.objects.get(class_name=class_name)
            try:
                Myclass.objects.create(class_name=new_class_name,class_member=u,is_activity=True)    #成员已加入班级时失败
            except:
                MyClassIndex.objects.filter(class_name=class_name,class_admin=u).delete()
                return JsonResponse({'data':0,'msg':'创建管理员失败'},safe=False)
            return JsonResponse({'data':1,'msg':'创建成功'},safe=False)
        except:
            MyClassIndex.objects.filter(class_name=class_name,class_admin=u).delete()
            return JsonResponse({'data':0,'msg':'创建失败'},safe=False)


    @method_decorator(ensure_csrf_cookie)
    def put(self,request):
        pass

class classApply(MyBaseView):
    def get(self,request):
        user_id=request.user.user_id
        print(user_id)
        try:
            myclass_data=MyClassIndex.objects.get(class_admin=user_id)
        except:
            return JsonResponse({"data":1,'msg':'无申请人员'})
        class_instance=MyClassIndex.objects.get(class_name=myclass_data)
        try:
            class_member=Myclass.objects.filter(class_name=class_instance,is_activity=False)
            newdata=[]
            for item in class_member:
                newitem={}
                newitem['class_member']=item.class_member.user_id
                newitem['user_name']=item.class_member.user_name
                newitem['class_name']=item.class_name.class_name
                newdata.append(newitem)
            return JsonResponse(newdata,safe=False)
        except:
            return JsonResponse({"data":0,'msg':'参数错误'})

    def post(self,request):
        data=request.data
        class_member=data.get('class_member')
        try:
            Myclass.objects.filter(class_member=class_member).update(is_activity=True)
            return JsonResponse({'data':1,'msg':'更新成功'})
        except:
            return JsonResponse({'data':0,'msg':'更新失败'})


class classMemeber(MyBaseView):
    def get(self,request):
        data=request.data
        class_name=data.get('class_name')
        try:
            class_instance=MyClassIndex.objects.get(class_name=class_name)
            class_member=Myclass.objects.filter(class_name=class_instance,is_activity=True)
            newdata=[]
            for item in class_member:
                newitem={}
                newitem['class_member']=item.class_member.user_id
                newitem['user_name']=item.class_member.user_name
                newitem['class_name']=item.class_name.class_name
                newdata.append(newitem) 
            return JsonResponse(newdata,safe=False)
        except:
            return JsonResponse({'data':0,'msg':'参数错误'})

    def post(self,request):
        data=request.data
        user_id=request.user.user_id
        try:
            user=User.objects.get(user_id=user_id)
        except:
            return JsonResponse({"data":0,"msg":'请先登录'})
        class_name=data.get('class_name')
        class_name=MyClassIndex.objects.get(class_name=class_name)
        try:
            Myclass.objects.create(class_name=class_name,class_member=user)
        except:
            return JsonResponse({'data':0,'msg':'申请失败'})
        return JsonResponse({'data':1,'msg':'申请成功，等待管理员审核'})