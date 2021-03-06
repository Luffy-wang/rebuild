from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from ..models import Problem
from account.models import User
import os
import zipfile
import hashlib
import json
from ..serializers import ProblemSerializers
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from utils.api.utils import MyBaseView,MyLoginrequired
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View

#@csrf_exempt
#@api_view(["GET","POST"])
#@login_required

# class Index(MyLoginrequired,MyBaseView):
#     #@login_required
#     def get(self,request):
#         #user=request.user
#         #return HttpResponse(user)
#         return #render(request,"problem/indexTest.html")

# class Problemindex(MyLoginrequired,MyBaseView):
#     #@method_decorator(ensure_csrf_cookie)
#     #@login_required
#     def get(self,request):
#         data=request.user
#         if(data.is_anonymous):
#             return redirect('/')
#         problem=Problem.objects.all()
#         pagenum=super(Problemindex,self).page_num(problem)
#         #return JsonResponse(pagenum,safe=False)
#         page_num=[]
#         for i in range(pagenum):
#             page_num.append(i)
#         return render(request,'problem/problemlist.html',{"pagenum":page_num})


class ProblemClass(MyBaseView):
    #@method_decorator(ensure_csrf_cookie)
    def get(self,request):
        page=request.data.get('page')
        problem=Problem.objects.all()
        data=super(ProblemClass,self).paginator_data(problem,page)
        serializer=ProblemSerializers(data,many=True)
        
        return JsonResponse(serializer.data,safe=False)
    def post(self,request):
        data=request.data
    
        _id=data.get("_id")
        if not _id:
            return JsonResponse({"data":"id is required"},safe=False)
        
        tags=data.get("tag")
        if not tags:
            return JsonResponse({"data":"tag is required"},safe=False)
        
        serializer=ProblemSerializers(data=data)
        data["test_case_id"]=_id

        if Problem.objects.filter(_id=_id).exists():   #更新
            pro=Problem.objects.get(_id=_id)
            serializer=ProblemSerializers(pro,data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"data":1,'msg':'更新成功'},safe=False)
            else:
                return JsonResponse({"data":0,'msg':'更新失败'},safe=False)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":1,'msg':'创建成功'},safe=False)  #todo modify 
        else:      
            return JsonResponse({"data":0,'msg':'创建失败'},safe=False)       

class ProblemDetail(MyBaseView):
    @method_decorator(ensure_csrf_cookie)
    def get(self,request):
        data=request.data
        problem_id=data.get("problem_id")
        #page=data.get("page")
        if not problem_id:
            return HttpResponse("problem id is required")
        problem_data=get_object_or_404(Problem,_id=problem_id)
        serializer=ProblemSerializers(problem_data)
        return JsonResponse(serializer.data,safe=False)
    @method_decorator(ensure_csrf_cookie)
    def delete(self,request):
        data=request.data
    
    
        for item in data.get("problem_id"):
            p=Problem.objects.get(_id=item)
            if p:
                problem=Problem.objects.filter(_id=item).delete()
                return JsonResponse({"data":1},safe=False)
            else:
                return JsonResponse({"data":0},safe=False)



class UploadTestCase(View):
    #@method_decorator(ensure_csrf_cookie)
    def post(self,request):
        test_case_id=request.POST.get("_id")
        test_case_dir=os.path.join("/test_case",test_case_id)
        os.mkdir(test_case_dir)
        file=request.FILES["fileupload"]
        tmp_file=os.path.join("/tmp",test_case_id+".zip")
        
        
        with open(tmp_file,"wb") as f:
            for chunk in file:
                f.write(chunk)
        try:
            zip_file=zipfile.ZipFile(tmp_file)
        except zipfile.BadZipFile:
            return HttpResponse("the zip file is bad")
        name_list=zip_file.namelist()
        
        md5_cache={}
        size_cache={}

        for item in name_list:
            with open(os.path.join(test_case_dir,item),"wb") as f:
                content=zip_file.read(item).replace(b"\n\n",b"\n")
                size_cache[item]=len(content)
                if item.endswith(".out"):
                    md5_cache[item]=hashlib.md5(content.rstrip()).hexdigest()

                f.write(content)
        test_case_info={"spj":False,"test_cases":{}}

        name_list=zip(*[name_list[i::2] for i in range(2)])
        for index,item in enumerate(name_list):
            data={"stripped_output_md5":md5_cache[item[1]],
                "input_size":size_cache[item[0]],
                "output_size":size_cache[item[1]],
                "input_name":item[0],
                "output_name":item[1]
            }
            ret=[]
            ret.append(data)
            test_case_info["test_cases"][str(index+1)]=data

        with open(os.path.join(test_case_dir,"info"),"w",encoding="utf-8")as f:
            f.write(json.dumps(test_case_info,indent=4))
        return JsonResponse({"data":1},safe=False)
