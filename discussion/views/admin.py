import json

from django.core import serializers
from django.shortcuts import render

from account.models import User
from discussion.models import Discussion, DiscussionFollow
from problem.models import Problem
from utils.api.utils import MyBaseView
from django.http import HttpResponse,JsonResponse


class discussion(MyBaseView):

    def addpage(request, problem_id):
        try:
            problem = Problem.objects.get(_id=problem_id)
            discussion_set = Discussion.objects.filter(problem_id=problem)
            discussion_data = serializers.serialize("json", discussion_set)
            discussion_data = json.loads(discussion_data)
            data = []
            for discussion in discussion_data:
                discussion2 = Discussion.objects.get(id=discussion['pk'])
                follow_set = DiscussionFollow.objects.filter(discussion=discussion2)
                follow_data = serializers.serialize("json", follow_set)
                follow_data = json.loads(follow_data)
                discussion["follow"] = follow_data
                data.append(discussion)

            return render(request, "discussion/addDiscussion.html", {"data": data, "problem_id": problem_id})
        except Exception as e:
            JsonResponse({"code": 1, "message": str(e)})
        return JsonResponse({"code": 1, "message": "unknown error"})

    def post(self, request):
        data=request.data
        print(data["problem_id"])
        try:
            problem=Problem.objects.get(_id=data["problem_id"])
        except Exception as e :
            JsonResponse({"code": 1, "message":str(e)},safe=False)
        if data["discussion_id"] is not 0:

            try:
                 discussion=Discussion.objects.get(id=data["discussion_id"])
                 print(discussion)
                 df=DiscussionFollow.objects.create(content=data["content"],discussion=discussion)
                 df.follow_user.add(request.user)
                 df.save()
            except Exception as e :
                JsonResponse({"code": 1, "message":str(e)},safe=False)
        else:
            try:
                Discussion.objects.create(created_user=request.user,content=data["content"],problem_id=problem)
            except Exception as e:
                return JsonResponse({"code": 1, "message":str(e)})
        return JsonResponse({"code": 0, "message":"submit success"})

    def delete(self,request):
        data=request.data
        print(request.user.user_type)
        print(request.user)
        discussion_id=data["discussion_id"]
        follow_id=data["follow_id"]
        if request.user.user_type=='Teacher':
            if follow_id == 0:
                try:
                    Discussion.objects.get(id=discussion_id).delete()
                except Exception as e :
                    JsonResponse({"code": 1, "message": str(e)})
            else:
                try:
                    DiscussionFollow.objects.get(id=follow_id).delete()
                except Exception as e :
                    JsonResponse({"code": 1, "message": str(e)})
        return JsonResponse({"code": 0, "message": "delete success"})