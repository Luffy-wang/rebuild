from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from ..models import Problem
import os
import zipfile
# from ..serialization import UploadForm
import hashlib
import json
from ..serializers import ProblemSerializers
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

    # def get(self,request):
    #     self.question_id=request.GET.get["problem"]
    #     if not question_id:
    #         return self.error("parameter error,problem id is required")
    #     try:
    #         get_object_or_404(Problem,_id=self.question_id)
    #     except Problem.DoesNotExist:
    #         raise Http404("problem is not exist")
    #     return self.success()#todo return json data

# class CreateProblem(APIView):
@api_view(["GET","POST"])
def post(request):
    # problem=Problem.objects.all()
    # serializer=ProblemSerializers(problem,many=True)
    # return JsonResponse(serializer.data,safe=False)
    data=request.POST.get("_id")
    _id=data
    if not _id:
        return HttpResponse("id is required")
    
    if Problem.objects.filter(_id=_id).exists():
        return HttpResponse("duplicate problem_id")
    tags=request.POST.get("tag")
    if not tags:
        return HttpResponse("tag is required")
        
    serializer=ProblemSerializers(data=request.data)
    
    if serializer.is_valid():   
        serializer.save()
    return JsonResponse(serializer.data)  #todo modify 

def get(request):
    #_id=request.GET.get("_id")
    problem=Problem.objects.all()
    serializer=ProblemSerializers(problem,many=True)
    
    return JsonResponse(serializer.data,safe=False)

def test(request):
    return render(request,"problem/upload.html")

@api_view(["GET","POST"])
def problem_detail(request,problem_id):
    #problem_id=request.GET.get("problem_id")
    if not problem_id:
        return HttpResponse("problem id is required")
    problem_data=get_object_or_404(Problem,_id=problem_id)
    serializer=ProblemSerializers(problem_data)
    return JsonResponse(serializer.data,safe=False)

def UploadTestCase(request):
    #test_case_id=request.POST.get["test_case_id"]
    test_case_dir=os.path.join("/test_case","2")
    os.mkdir(test_case_dir)
    #file=UploadForm(request.FILES)
    file=request.FILES["fileupload"]
    #filea=bytes(file,encoding="utf-8")
    tmp_file=os.path.join("/tmp","2"+".zip")
    
    
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
    test_case_info={"spj":"false","test_cases":{}}

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
    return HttpResponse("finish upload")