import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator


class JSONParse(object):
    @staticmethod
    def parse(body):
        return json.loads(body.decode('utf-8'))


class MyBaseView(View):
    def _get_request_data(self,request):
        if request.method not in ['GET','DELETE']:
            body=request.body
            #return HttpResponse(body)
            if body:
                return JSONParse.parse(body)
            return {}
        return request.GET

    def dispatch(self,request,*args,**kwargs):
        try:
            request.data=self._get_request_data(self.request)
        except ValueError as e:
            return HttpResponse("error")
        return super(MyBaseView,self).dispatch(request,*args,**kwargs)

class CSRFExemptMyBaseView(MyBaseView):
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super(CSRFExemptMyBaseView,self).dispatch(request,*args,**kwargs)