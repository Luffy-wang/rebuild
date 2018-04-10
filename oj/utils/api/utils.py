import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from django_redis import get_redis_connection
from django_redis.cache import RedisCache
from django_redis.client.default import DefaultClient
from django.core.cache import cache

class MyRedis(DefaultClient):
    def __getattr__(self,item):
        client=self.get_client(write=True)
        return getattr(client,item)

    # def get_incr(self,key,count=1):
    #     client=self.get_client(write=True)
    #     return client.get_incr()


class JSONParse(object):
    @staticmethod
    def parse(body):
        return json.loads(body.decode('utf-8'))


class MyBaseView(View):
    def _get_request_data(self,request):
        if request.method not in ['GET','DELETE']:
            
            body=request.body
            #content_type = request.META.get("CONTENT_TYPE")
            #return HttpResponse(body)
            if body:
                return JSONParse.parse(body)
            #return {}
        
        return request.GET

    def dispatch(self,request,*args,**kwargs):
        try:
            request.data=self._get_request_data(self.request)
        except ValueError as e:
            return HttpResponse("error")
        #try:
        return super(MyBaseView,self).dispatch(request,*args,**kwargs)
        # except Exception as e:
        #     return HttpResponse(e)

class CSRFExemptMyBaseView(MyBaseView):
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super(CSRFExemptMyBaseView,self).dispatch(request,*args,**kwargs)