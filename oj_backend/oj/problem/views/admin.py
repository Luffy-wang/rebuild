from django.http import HttpResponse
from django.shortcuts import render
from ..models import Problem
import os
import zipfile
from ..serialization import UploadForm
import hashlib
import json
    # def get(self,request):
    #     self.question_id=request.GET.get["problem"]
    #     if not question_id:
    #         return self.error("parameter error,problem id is required")
    #     try:
    #         get_object_or_404(Problem,_id=self.question_id)
    #     except Problem.DoesNotExist:
    #         raise Http404("problem is not exist")
    #     return self.success()#todo return json data
 
def post(request):
    data=request.POST.get("_id")
    _id=data
    if not _id:
        return HttpResponse("id is required")
    #title=data["title"]
    # if not title:
    #     return self.error("title is required")
    title=request.POST.get("title")
    description=request.POST.get("de")
    input_d=request.POST.get("inputds")
    out_d=request.POST.get("outputds")
    t_i=request.POST.get("t_id")
    tag=request.POST.get("tag")
    languages=request.POST.get("languages")
    create_time=request.POST.get("c_t")
    t_l=request.POST.get("t_l")
    m_l=request.POST.get("m_l")
    if Problem.objects.filter(_id=_id).exists():
        return HttpResponse("duplicate problem_id")
    # tags=data["tags"]
    # if not tags:
    #     return self.error("tag is required")
        
    #data["created_by"]=request.user
    data={"_id":_id,"title":title,"description":description}
    try:
        problem=Problem.objects.create(**data)
    except:
        return HttpResponse("error")

    return HttpResponse("end success")

def get(request):
    return render(request,"problem/indexTest.html")

def test(request):
    return render(request,"problem/upload.html")

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