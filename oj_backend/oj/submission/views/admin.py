from rest_framework.decorators import api_view
import requests
import hashlib
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,get_object_or_404
from submission.languages import c_lang_config
from problem.models import Problem
from problem.serializers import ProblemSerializers
from ..serializers import SubmissionSerializer,ClassHomeworkSerializer,HomeworkItemSerializer
from ..models import Submission,ClassHomework,Homework_item
import json
from django.views.decorators.csrf import csrf_exempt
from account.models import Myclass,User
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
#@api_view(["GET","POST"])
#@login_required      todo
@csrf_exempt
@login_required
def post(request):
    
    

    #code=request.POST.get("code")
    data=json.loads(request.body.decode("utf-8"))
    code=data["code"]
    class_name=data['class_name']
    problem_id=data['problem_id']
    homework_item=data['homework_item']
    student_id=data['student_id']
    problem_data=get_object_or_404(Problem,_id=problem_id)
    serializers=ProblemSerializers(problem_data)
    max_cpu_time=serializers.data["time_limit"]
    max_memory=serializers.data["memory_limit"]
    test_case_id=serializers.data["test_case_id"]
    problem_id1=serializers.data['_id']
    #send token
    send="123456"
    token=hashlib.sha256(send.encode("utf-8")).hexdigest()
    kwargs={"headers":{"X-Judge-Server-Token":token,
                        "Content-Type":"application/json"}}
    #code="#include<stdio.h>\r\nint main()\r\n{\r\nprintf(\"3\");\r\n}"
    # c_src=r"""
    # include<stdio.h>
	# int main()
	# {
	# printf("3");
	# }
	# """
    data={
        "language_config":c_lang_config,#todo
        "src":code,
        "max_cpu_time":1000,#max_cpu_time,
        "max_memory":1024*1024*128,#todo eddit memory
        "test_case_id":'normal',#test_case_id,
        "output":True,
        "spj_version":None,
        "spj_config":None,
        "spj_compile_config":None,
    }
    #return JsonResponse(data,safe=False)
    kwargs["data"]=json.dumps(data) #convert to str
    
    r=requests.post("http://127.0.0.1:8088/judge",**kwargs).json()
    #return JsonResponse(r,safe=False)
    try:
        result=r["data"][0]["result"]
    except TypeError:
        return JsonResponse(r,safe=False)

    

    submission_list={
        "result":result,
        "problem_id":problem_id1,#problem_id,
        "code":code,
        "language":"c",#todo
        "class_name":class_name,#todo
        "user_id":student_id,
        "homework_item":homework_item
        #"user_name":"nood",#todo
    }
    serializers1=SubmissionSerializer(data=submission_list)
    if serializers1.is_valid():
        serializers1.save()
        return JsonResponse(serializers1.data,safe=False)

def get(request):
    return render(request,"submission/submission_list.html")

# required teacher
@csrf_exempt
def addProblemToClass(request):
    data=json.loads(request.body.decode("utf-8"))
    class_name=data["class_name"]
    problem_id=data["problem_id"]
    homework_item=data['homeword_item']
    c=Myclass.objects.filter(class_name=class_name)
    p=Problem.objects.get(_id=problem_id)
    if c and p:
        problem_title=model_to_dict(p)["title"]
        class_homework=ClassHomework.objects.create(class_name=class_name,problem_id=p,problem_title=problem_title,homework_item=homework_item)
        return JsonResponse({"data":"1"})
    else:
        return JsonResponse({"data":"0"})

@csrf_exempt
def showClassProblem(request):
    data=json.loads(request.body.decode("utf-8"))
    class_name=data["class_name"]
    homework_item=data['homework_item']
    data=ClassHomework.objects.filter(class_name=class_name,homework_item=homework_item)
    serializer=ClassHomeworkSerializer(data,many=True)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def createHomeworkItem(request):
    data=json.loads(request.body.decode('utf-8'))
    class_name=data['class_name']
    homework_item=data['homework_item']
    homework_item_title=data['homework_item_title']
    mylist={'class_name':class_name,'homework_item':homework_item,'home_item_title':homework_item_title}
    #homework=Homework_item.objects.create(class_name=class_name,homework_item=homework_item)
    serializer=HomeworkItemSerializer(data=mylist)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':1},safe=False)
    else:
        return JsonResponse({'data':0},safe=False)
@csrf_exempt
def showHomeworkItem(request):
    #data=json.loads(request.body.decode('utf-8'))
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
@csrf_exempt
def testuserobject(request):
    #return JsonResponse({"data":0},safe=False)
    user_id=request.user.user_id
    return JsonResponse({"data":user_id},safe=False)

#required join class
@csrf_exempt
def showSampleSubmission(request):
    data=json.loads(request.body.decode("utf-8"))
    user_id=data["user_id"]
    problem_id=data['problem_id']
    homework_item=data['homework_item']
    #problem_title=Problem.objects.get(_id=problem_id)
    if problem_id is '':
        submission=Submission.objects.filter(user_id=user_id)
        serializer=SubmissionSerializer(submission,many=True)
        return JsonResponse(serializer.data,safe=False)
    else:
        if homework_item is '':
            submission=Submission.objects.filter(user_id=user_id,problem_id=problem_id)
            serializer=SubmissionSerializer(submission,many=True)
            return JsonResponse(serializer.data,safe=False)
        else:
            submission=Submission.objects.filter(user_id=user_id,problem_id=problem_id,homework_item=homework_item)
            serializer=SubmissionSerializer(submission,many=True)
            return JsonResponse(serializer.data,safe=False)
            
        



