from rest_framework.decorators import api_view

@api_view(["GET","POST"])
#@login_required      todo
def post(request):
    data=request.data
    
