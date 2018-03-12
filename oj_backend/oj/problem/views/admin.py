from django.http import HttpResponse

class ProblemCreated():
    # def get(self,request):
    #     self.question_id=request.GET.get["problem"]
    #     if not question_id:
    #         return self.error("parameter error,problem id is required")
    #     try:
    #         get_object_or_404(Problem,_id=self.question_id)
    #     except Problem.DoesNotExist:
    #         raise Http404("problem is not exist")
    #     return self.success()#todo return json data
        
    def post(self,request):
        data=request.data
        _id=data["_id"]
        if not _id:
            return self.error("id is required")
        title=data["title"]
        if not title:
            return self.error("title is required")
        if Problem.objects.filter(_id=_id).exists():
            return self.error("duplicate problem_id")
        tags=data["tags"]
        if not tags:
            return self.error("tag is required")
        
        data["created_by"]=request.user

        problem=Problem.objects.create(**data)

        return self.success()




