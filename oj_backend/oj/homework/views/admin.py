from utils.api.utils import MyBaseView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from account.models import User
from myclass.models import Myclass
from ..models import Homework_item
from ..serializer import HomeworkItemSerializer,ClassHomeworkSerializer



class HomeworkItem(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        if not User.is_teacher(request.user) or User.is_admin(request.user):
            teacheruser=Myclass.objects.get(class_member=request.user.user_id)
            teacheruser=model_to_dict(teacheruser)
            class_name=teacheruser["class_name"]
        else:
            return JsonResponse({"data":0},safe=False)
        try:
            homeworkitem=Homework_item.objects.filter(class_name=class_name)
            serializer=HomeworkItemSerializer(homeworkitem,many=True)
            return JsonResponse(serializer.data,safe=False)
        except:
            return JsonResponse({'data':0},safe=False)

    @method_decorator(ensure_csrf_cookie)
    def post(self,request):
        
        user=request.user.user_id
        myclass=Myclass.objects.get(class_member=user)
        myclass=model_to_dict(myclass)
        class_name=myclass['class_name']
        #class_name=data["class_name"]
        homework_item=data['homework_item']
        homework_item_title=data['homework_item_title']
        mylist={'class_name':class_name,'homework_item':homework_item,"homework_item_title":homework_item_title}
        #homework=Homework_item.objects.create(class_name=class_name,homework_item=homework_item)
        serializer=HomeworkItemSerializer(data=mylist)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data':1},safe=False)
        else:
            
            return JsonResponse({'data':0},safe=False)

    @method_decorator(ensure_csrf_cookie)
    def delete(self,request):
        data=request.data
        homework_item=data.get("homework_item")
        h=Homework_item.objects.get(homework_item=homework_item)
        if h:
            Homework_item.objects.filter(homework_item=homework_item).delete()
            return JsonResponse({"data":1},safe=False)
        else:
            return JsonResponse({"data":0},safe=False)


class ClassProblemItem(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        
        user=request.user.user_id
        myclass=Myclass.objects.get(class_member=user)
        myclass=model_to_dict(myclass)
        class_name=myclass["class_name"]
        homework_item=data['homework_item']
        data=ClassHomework.objects.filter(class_name=class_name,homework_item=homework_item)
        serializer=ClassHomeworkSerializer(data,many=True)
        return JsonResponse(serializer.data,safe=False)

    @method_decorator(ensure_csrf_cookie)
    def post(self,request):
        data=request.data
        class_name=data.get("class_name")

        homework_item=data.get('homework_item')
        
        for item in data.get("problem"):
            problem_id=item
            
            c=Myclass.objects.filter(class_name=class_name)
            p=Problem.objects.get(_id=problem_id)
            homework_item=Homework_item.objects.get(homework_item=homework_item)

            if c and p:
                problem_title=model_to_dict(p)["title"]
                class_homework=ClassHomework.objects.create(class_name=class_name,problem_id=p,problem_title=problem_title,homework_item=homework_item)
            else:
                return JsonResponse({"data":"0"})
        return JsonResponse({"data":1},safe=False)

    @method_decorator(ensure_csrf_cookie)
    def delete(self,request):
        data=request.data
        homework_item=data.get("homework_item")
        for item in data.get("problem"):
            problem_id=item
            p=Problem.objects.get(_id=problem_id)
            if p:
                class_homework=ClassHomework.objects.filter(problem_id=problem_id).delete()
            else:
                return JsonResponse({"data":0},safe=False)  
        return JsonResponse({"data":1},safe=False)