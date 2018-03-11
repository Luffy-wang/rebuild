from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
import hashlib
import json
import requests
from .models import Question
# Create your views here.


	
def ping(request):
	send="123456"
	token=hashlib.sha256(send.encode("utf-8")).hexdigest() #return 0x
	kwargs={"headers":{"X-Judge-Server-Token":token,
						"Content-Type":"application/json"}}
	t=requests.post('http://127.0.0.1:8088/ping',**kwargs).json()
	return HttpResponse(json.dumps(t),content_type="application/json")

def detail(request,question_id):
	try:
		q=Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request,"account/detail.html",{"question":q})

def results(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,"account/results.html",{"question":question})

def vote(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		select_choice=question.choice_set.get(pk=request.POST["choice"])
	except(KeyError,Choice.DoseNotExist):
		return render(request,"account/detail",{"question":question,"error_message":"you didn't select a choice",})
	else:
		select_choice.votes +=1
		select_choice.save()
		return HttpResponseRedirect(reverse("account:results",args=(question_id,)))

def index(request):
	latest_question_list=Question.objects.order_by("-pub_date")[:5]
	template=loader.get_template("account/index.html")
	context={
	"latest_question_list":latest_question_list,
	}
	return HttpResponse(template.render(context,request))
	#output=",".join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)

def judge(request):
	send="123456"
	token=hashlib.sha256(send.encode("utf-8")).hexdigest() #return 0x
	kwargs={"headers":{"X-Judge-Server-Token":token,
						"Content-Type":"application/json"}}

	c_src=r"""
	#include<stdio.h>
	int main()
	{
	int a,b;
	scanf("%d%d",&a,&b);
	printf("%d\n",a+b);
	return 0;
	}
	"""

	c_lang_config={
	"compile":{
	"src_name":"main.c",
	"exe_name":"main",
	"max_cpu_time":3000,
	"max_real_time":5000,
	"max_memory":1024*1024*128,
	"compile_command":"/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c99 {src_path} -lm -o {exe_path}",
	},
	"run":{
	"command":"{exe_path}",
	"seccomp_rule":"c_cpp",
	"env":["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]
	}
	}

	data={
	"language_config":c_lang_config,
	"src":c_src,
	"max_cpu_time":1000,
	"max_memory":1024*1024*128,
	"test_case_id":"normal",
	"output":True,
	"spj_version":None,
	"spj_config":None,
	"spj_compile_config":None
	}
	kwargs["data"]=json.dumps(data)
	t=requests.post("http://127.0.0.1:8088/judge",**kwargs).json()
	return HttpResponse(json.dumps(t),content_type="application/json")