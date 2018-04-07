from utils.api.utils import MyBaseView
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from account.models import Myclass
from account.serializer import MyclassSerializer,ShowClassSerializer
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