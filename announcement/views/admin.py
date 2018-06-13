from django.shortcuts import render, redirect
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from utils.api.utils import MyBaseView
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from announcement.models import Announcement
from announcement.serializer import AnnouncementSerializer
from django.core import serializers
import time
from django.utils import timezone

class announcement(MyBaseView):

    def addpage(request):
        data = request.user
        if (data.is_anonymous):
            return redirect('/')
        return render(request, "announcement/addAnnouncement.html")




    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        print(request.data,type(request.data))
        serializer = AnnouncementSerializer(data=request.data)
        # print(serializer.is_valid(),serializer.errors)
        # print(request.POST.get('title'))
        if serializer.is_valid():
            data = serializer.data
            try:
                 Announcement.objects. \
                    create(title=data["title"], content=data["content"], is_public=data["is_public"],
                            created_user_id=request.user.user_id)
            except Exception as e:
                return JsonResponse({"code":1,"message": str(e)}, safe=False)
        else:
            return JsonResponse({"code":1,"message": serializer}, safe=False)
        return JsonResponse({"code": 0,"message":"submit success"}, safe=False)

    def get(self,request):
        try:
            announcement_set = Announcement.objects.all()
        except Exception as e:
            return JsonResponse({"code":1,"message": str(e)}, safe=False)
        data = serializers.serialize("json", announcement_set)
        data = json.loads(data)
        return render(request, "announcement/announcementList.html", {"data": data})

    # @method_decorator(ensure_csrf_cookie)
    def updateannouncement(request, id):

        try:
            announcement_set = Announcement.objects.filter(id=id)
        except Exception as e:
            return JsonResponse({"code":1,"message": str(e)}, safe=False)
        if request.method == 'GET':
            data = serializers.serialize("json", announcement_set)
            data = json.loads(data)
            # print(data[0])
            return render(request, "announcement/updateAnnouncement.html", {"data": data[0]})

        else:
            data = json.loads(request.body.decode('utf-8'))
            serializer = AnnouncementSerializer(data=data)
            created_user_id = 1
            created_time = timezone.now()
            if serializer.is_valid():
                data = serializer.data
                try:
                    Announcement.objects.filter(id=id). \
                        update(title=data["title"], content=data["content"], is_public=data["is_public"],
                               created_time=created_time, created_user_id=created_user_id)
                except Exception as e:
                    return JsonResponse({"code":1,"message": str(e)}, safe=False)

            else:
                return JsonResponse({"code":1,"message": "serialized failed"}, safe=False)

        return JsonResponse({"code": 0,"message":"update success"}, safe=False)
    def delete(request,id):
        if request.user.user_type=='Teacher':
            try:
                Announcement.objects.filter(id=id).delete()
            except Exception as e:
                return JsonResponse({"code":1,"message": str(e)}, safe=False)
        else:
            return JsonResponse({"code":1,"message": "user is not a admin or is null"}, safe=False)
        return JsonResponse({"code": 0,"message":"delete success"}, safe=False)
