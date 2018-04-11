#from rest_framework.decorators import api_view
import requests
import hashlib
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,get_object_or_404
from submission.languages import c_lang_config
from problem.models import Problem
from problem.serializers import ProblemSerializers
from ..serializers import SubmissionSerializer
from ..models import Submission
import json
from utils.api.utils import MyBaseView
#from django.views.decorators.csrf import csrf_exempt
from account.models import User
from myclass.models import Myclass
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
import os
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.cache import cache
from judgermanage.dispatch import JudgerManageBase
#@api_view(["GET","POST"])
#@login_required      todo
# @csrf_exempt
# @login_required

class SubmissionClass(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        data=request.data
       
        # cache.set("name2","kwq",timeout=40)
        # name=cache.get("name1")
        # return HttpResponse(name)
        user_id=request.user.user_id
        
        problem_id=data.get('problem_id')
        homework_item=data.get('homework_item')
        
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



    #@method_decorator(ensure_csrf_cookie)
    def post(self,request):
        data=request.data
        code=data.get("code")
        class_name=data.get('class_name')
        problem_id=data.get('problem_id')
        homework_item=data.get('homework_item')
        student_id=request.user.user_id
        problem_data=get_object_or_404(Problem,_id=problem_id)# warning: if problem not exist it will return 404
        serializers=ProblemSerializers(problem_data)
        max_cpu_time=serializers.data["time_limit"]
        max_memory=serializers.data["memory_limit"]
        test_case_id=serializers.data["test_case_id"]
        problem_id1=serializers.data['_id']
        problem_language=serializers.data["tag"]

        send="123456"#os.environ(sendToken)
        token=hashlib.sha256(send.encode("utf-8")).hexdigest()
        kwargs={"headers":{"X-Judge-Server-Token":token,
                        "Content-Type":"application/json"}}

        data={
        "language_config":c_lang_config,#todo
        "src":code,
        "max_cpu_time":max_cpu_time,
        "max_memory":1024*1024*max_memory,#todo eddit memory
        "test_case_id":test_case_id,#test_case_id,
        "output":True,
        "spj_version":None,
        "spj_config":None,
        "spj_compile_config":None,
        }

        kwargs["data"]=json.dumps(data)
        #posted=JudgerManageBase(**kwargs).judger_dispatch()
        r=requests.post("http://127.0.0.1:8088/judge",**kwargs).json()
        #result=r["data"].sort(k=lambda x:int(x["test_cae"]))
        
        try:
            if r["err"]:
                return JsonResponse(r["err"],safe=False)
            else:
                result=r["data"].sort(k=lambda x:int(x["test_cae"]))
            #result=r["data"][0]["result"]
        except TypeError:
            return JsonResponse(r,safe=False)

        submission_list={
        "result":result,
        "problem_id":problem_id1,#problem_id,
        "code":code,
        "language":problem_language,#"c",#todo
        "class_name":class_name,#todo
        "user_id":student_id,
        "homework_item":homework_item
        #"user_name":"nood",#todo
        }   

        serializers1=SubmissionSerializer(data=submission_list)
        if serializers1.is_valid():
            serializers1.save()
        return JsonResponse(serializers1.data,safe=False)





            
        



