from django.urls import path
from .views import admin


urlpatterns=[
    path("submission/",admin.get,name="submission_index"),
    path("submission/<int:_id>",admin.post,name="submission"),   
]