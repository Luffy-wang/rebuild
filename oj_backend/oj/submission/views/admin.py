from rest_framework.decorators import api_view
import requests
import hashlib
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,get_object_or_404
from submission.languages import c_lang_config
from problem.models import Problem
from problem.serializers import ProblemSerializers
from ..serializers import SubmissionSerializer
import json


@api_view(["GET","POST"])
#@login_required      todo
def post(request,_id):
    data=request.data
    
    _id=data["id"]
    code=data["code"]
    
    problem_data=get_object_or_404(Problem,_id=_id)
    serializers=ProblemSerializers(problem_data)
    max_cpu_time=serializers.data["time_limit"]
    max_memory=serializers.data["memory_limit"]
    test_case_id=serializers.data["test_case_id"]
    
    #send token
    send="123456"
    token=hashlib.sha256(send.encode("utf-8")).hexdigest()
    kwargs={"headers":{"X-Judge-Server-Token":token,
                        "Content-Type":"application/json"}}
    
    # c_src=r"""
    # #include<stdio.h>
	# int main()
	# {
	# int a,b;
	# scanf("%d%d",&a,&b);
	# printf("%d\n",a+b);
	# return 0;
	# }
	# """
    data={
        "language_config":c_lang_config,#todo
        "src":code,
        "max_cpu_time":max_cpu_time,
        "max_memory":1024*1024*128,#todo eddit memory
        "test_case_id":test_case_id,
        "output":True,
        "spj_version":None,
        "spj_config":None,
        "spj_compile_config":None,
    }
    kwargs["data"]=json.dumps(data) #convert to str
    r=requests.post("http://127.0.0.1:8088/judge",**kwargs).json()
    result=r["data"][0]["result"]
    
    if result==0:
        submission_list={
            "result":result,
            "problem_id":_id,
            "code":code,
            "language":"c",#todo
            "class_name":"1ban",
            "user_id":request.data["user_id"],
            "user_name":"nood",
            
        }
    serializers1=SubmissionSerializer(data=submission_list)
    if serializers1.is_valid():
        serializers1.save()
        
    return JsonResponse(serializers1.data)

def get(request):
    return render(request,"submission/submission_list.html")
    