from django.core.cache import cache
from django.http import HttpResponse,JsonResponse
import requests
#from django.

class JudgerManageBase(object):
    def __init__(self,**data):
        self.data=data
        self.i=0
        #self.judgercount=cache.set("judgerservercount",self.i)
        
    def chose_judger(self):
        self.judgercount=cache.set("judgerservercount",self.i)
        cache.persist("judgerservercount")

        
    def judger_dispatch(self):
        #return JsonResponse(self.data,safe=False)
        
        
        self.judgercount=cache.get("judgerservercount")
        if self.judgercount<0:
            cache.set("judgerservercount",self-1)
            cache.persist("judgerservercount")
            # send=os.environ(sendToken)
            # token=hashlib.sha256(send.encode("utf-8")).hexdigest()
            # kwargs={"headers":{"X-Judge-Server-Token":token,
            #             "Content-Type":"application/json"}}
            r=requests.post("http://127.0.0.1:8088/judge",**self.data).json()
            cache.set("judgerservercount",self.i+1)
            cache.persist("judgerservercount")
            return JsonResponse(r,safe=False)
        else:
            self.judgercount=cache.set("judgerservercount",self.i+1)
            return JsonResponse({"data":0},safe=False)
