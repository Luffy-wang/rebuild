from django.http import HttpResponse
from django.shortcuts import render
from ..models import Problem
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
    return HttpResponse("test")




