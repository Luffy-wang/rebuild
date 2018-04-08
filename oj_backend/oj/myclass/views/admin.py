from utils.api.utils import MyBaseView
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from account.models import User
from ..models import Myclass
from ..serializer import MyclassSerializer,ShowClassSerializer
from django.forms.models import model_to_dict

class Mycclass(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        #data=json.loads(request.body.decode("utf-8"))
    
        user_id=request.GET.get("userid")
        
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


    @method_decorator(ensure_csrf_cookie)
    def post(self,request):
        data=request.data
        #class_name=request.POST.get("class_name")
        class_name=data.get("class_name")
        user_id=data.get("user_id")
        #return HttpResponse(user_id)
        u=User.objects.get(user_id=user_id)
        if User.is_teacher(u):
            myclass=Myclass.objects.create(class_name=class_name,class_admin=u,class_member=u,is_activity=True)
            return JsonResponse({"data":1})
        elif User.is_admin(u):
            return HttpResponse("error action")
        else:
            c=Myclass.objects.filter(class_member=u)
            if c:
                return JsonResponse({"data":0})#already existed
            else:
                myclass=Myclass.objects.create(class_name=class_name,class_member=u,is_activity=True)
                return JsonResponse({"data":1})


    @method_decorator(ensure_csrf_cookie)
    def put(self,request):
        pass