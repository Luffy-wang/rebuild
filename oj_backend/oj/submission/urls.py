from django.urls import path
from .views import admin


urlpatterns=[
    path("",admin.get,name="submission_index"),
    path("<int:_id>",admin.post,name="submission"),   
]