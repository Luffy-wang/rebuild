from django.core.cache import cache
from django.http import HttpResponse,JsonResponse
import requests
from django_redis import get_redis_connection
import json
import re
#from django.
#todo test
class JudgerManageBase(object):
    def __init__(self,**data):
        self.data=data
        self.i=0
        #self.judgercount=cache.set("judgerservercount",self.i)
    con=get_redis_connection("default")
        
    

    def continue_process(self):
        if cache.llen("wattingsqueue"):
            from JudgerManage.dispatch import JudgerManageBase
            data=self.con.rpop("wattingsqueue")
            JudgerManageBase(data).judger_dispatch()

    def judger_dispatch(self):
        
        
        self.con.lpush("wattingsqueue",self.data)
        self.con.persist("wattingsqueue")
        #senddata=self.con.rpop("wattingsqueue").decode("utf-8")
        senddata=eval(self.con.rpop("wattingsqueue"))
        # return JsonResponse(senddata,safe=False)
        #load = json.loads(senddata)
        #return JsonResponse(fromdata,safe=False)
        
        
        r=requests.post("http://127.0.0.1:8088/judge",**senddata).json()
        
        return JsonResponse(r,safe=False)
       
