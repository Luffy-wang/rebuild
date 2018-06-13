from utils.api.utils import MyBaseView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from account.models import User,User_type
from myclass.models import Myclass,MyClassIndex
from problem.models import Problem
from ..models import Homework_item,ClassHomework
from ..serializer import HomeworkItemSerializer,ClassHomeworkSerializer
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict

class HomeworkIndex(MyBaseView):
    def get(self,request):
        data=request.user
        #return JsonResponse({'data':data},safe=False)
        if(data.is_anonymous):
            return redirect('/')
        homeworkitem=Homework_item.objects.all()
        pagenum=super(HomeworkIndex,self).page_num(homeworkitem)
        page_num=[]
        for i in range(pagenum):
            page_num.append(i)
        return render(request,'homework/homework_index.html',{"pagenum":page_num})

class HomeworkItem(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        if User.is_student(request.user):
            return JsonResponse({"data":0,'msg':'无相关权限'},safe=False)
        if  User.is_teacher(request.user) :#or User.is_admin(request.user):
            
            teacheruser=Myclass.objects.get(class_member=request.user.user_id)
            #teacheruser=model_to_dict(teacheruser)
            class_name=teacheruser.class_name
        else:
            return JsonResponse({"data":0,'msg':'not teacher or admin'},safe=False)


        #
        #homeworkitem=Homework_item.objects.filter(class_name=class_name)
        #return HttpResponse(homeworkitem)
        # 
        try:
            page=request.data.get('page')
            if User.is_admin(request.user):
                homeworkitem=Homework_item.objects.all()
            else:
                homeworkitem=Homework_item.objects.filter(class_name=class_name)
            homeworkitem=super(HomeworkItem,self).paginator_data(homeworkitem,page)
            serializer=HomeworkItemSerializer(homeworkitem,many=True)
            return JsonResponse(serializer.data,safe=False)
        except:
            return JsonResponse({'data':0,'msg':'参数错误'},safe=False)

    @method_decorator(ensure_csrf_cookie)
    def post(self,request):
        user=request.user.user_id
        data=request.data
        myclass=Myclass.objects.get(class_member=user)

        #myclass=model_to_dict(myclass)
        class_name=str(myclass.class_name)
        homework_item=data['homework_item']
        homework_item_title=data.get('homework_item_title')
        mylist={'class_name':class_name,'homework_item':homework_item,"homework_item_title":homework_item_title}
        serializer=HomeworkItemSerializer(data=mylist)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data':1,'msg':'创建成功'},safe=False)
        else:
            
            return JsonResponse({'data':0,'msg':serializer.errors},safe=False)

    @method_decorator(ensure_csrf_cookie)
    def delete(self,request):
        data=request.data
        homework_item=data.get("homework_item")
        h=Homework_item.objects.get(homework_item=homework_item)
        if h:
            Homework_item.objects.filter(homework_item=homework_item).delete()
            return JsonResponse({"data":1,'msg':'删除成功'},safe=False)
        else:
            return JsonResponse({"data":0,'msg':'删除失败'},safe=False)

class HomeworkList(MyBaseView):
    def get(self,request):
        user_id=request.user.user_id
        try:
            class_name=MyClassIndex.objects.get(class_admin=user_id).class_name
        except:
            return JsonResponse({'data':0,'msg':'不是班级管理员，无权操作'})
        class_item=Homework_item.objects.filter(class_name=class_name)
        serializer=HomeworkItemSerializer(class_item,many=True)
        return JsonResponse(serializer.data,safe=False)


class ClassProblemItem(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        
        user=request.user.user_id
        data=request.data
        myclass=Myclass.objects.get(class_member=user)
        #myclass=model_to_dict(myclass)
        class_name=myclass.class_name
        homework_item=data['homework_item']
        try:
            homework_item=Homework_item.objects.get(homework_item=homework_item)
        except:
            return JsonResponse({'data':0,'msg':'请求作业项不存在'})
        data=ClassHomework.objects.filter(class_name=class_name,homework_item=homework_item)
        serializer=ClassHomeworkSerializer(data,many=True)
        return JsonResponse(serializer.data,safe=False)

    @method_decorator(ensure_csrf_cookie)
    def post(self,request):
        data=request.data
        class_name=MyClassIndex.objects.get(class_admin=request.user.user_id)
        homework_item=data.get('homework_item')
        c=Myclass.objects.filter(class_name=class_name)
        homework_item=Homework_item.objects.get(homework_item=homework_item)
        for item in data.get("problem"):     #接收一个数组
            problem_id=item
            
            p=Problem.objects.get(_id=problem_id)
            
            if c and p:
                problem_title=p.title
                class_homework=ClassHomework.objects.create(class_name=class_name,problem_id=p,problem_title=problem_title,homework_item=homework_item)
            else:
                return JsonResponse({"data":0,'msg':'创建失败'})
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