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
import datetime

class SubmissionClass(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        data=request.data
        user_id=request.user.user_id
        
        problem_id=data.get('problem_id')
        #homework_item=data.get('homework_item')
        submission=Submission.objects.filter(user_id=user_id)
        for item in submission:
            item.create_time=item.create_time.strftime("%Y-%m-%d %H:%I:%S")
        serializer=SubmissionSerializer(submission,many=True)
        return JsonResponse(serializer.data,safe=False)

        #notice!!!
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
        myclass=Myclass.objects.filter(class_member=request.user.user_id).distinct()
        class_name=myclass[0].class_name.class_name
        problem_id=data.get('problem_id')
        
        homework_item=data.get('homework_item')
        student_id=request.user.user_id
        problem_data=get_object_or_404(Problem,_id=problem_id)# warning: if problem not exist it will return 404
        serializers=ProblemSerializers(problem_data)
        max_cpu_time=serializers.data["time_limit"]
        max_memory=serializers.data["memory_limit"]
        test_case_id=serializers.data["test_case_id"]
        problem_id1=serializers.data['_id']
        problem_language=data.get('language')

        send="123456"#os.environ(sendToken)
        token=hashlib.sha256(send.encode("utf-8")).hexdigest()
        kwargs={"headers":{"X-Judge-Server-Token":token}}
        c_src = r"""
        #include <stdio.h>
        int main(){
        int a, b;
        scanf("%d%d", &a, &b);
        printf("%d\n", a+b);
        return 0;
        }
        """
        data={
        "language_config":c_lang_config,#todo
        "src":code,
        "max_cpu_time":max_cpu_time,
        "max_memory":1024*1024*max_memory,
        "test_case_id":test_case_id,
        "output":True,
        "spj_version":None,
        "spj_config":None,
        "spj_compile_config":None,
        }
        
        kwargs["json"]=data
        start_time=datetime.datetime.now()
        
        r=requests.post("http://127.0.0.1:8090/judge",**kwargs).json()
        end_time=datetime.datetime.now()
        print(end_time-start_time) 
        try:
            if r["err"]:
                return JsonResponse(r["err"],safe=False)
            else:
                result=r["data"].sort(key=lambda x:int(x["test_case"]))
            #result=r["data"][0]["result"]
        except:
            return JsonResponse({'data':0,'msg':'判题服务器返回值错误'},safe=False)
        answer_result=0
        real_time=0
        for item in r['data']:
            if item['result']!=0:
                answer_result=item['result']
                break
            else:
                if real_time>item['real_time']:
                    real_time=item['real_time']
        
        submission_list={
        "result":answer_result,
        "problem_id":problem_id1,
        "code":code,
        "language":problem_language,
        "class_name":class_name,#班级名称
        "user_id":student_id,
        "homework_item":homework_item,
        'real_time':real_time
        }   

        serializers1=SubmissionSerializer(data=submission_list)
        if serializers1.is_valid():
            serializers1.save()
            return JsonResponse({'data':serializers1.data['result']},safe=False)
        else:
            return JsonResponse(serializers1.errors,safe=False)
        





            
        



