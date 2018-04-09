from django.urls import path
from django.conf.urls import url
from .views.admin import Mycclass


urlpatterns=[
    url(r"^showclass/?$",Mycclass.as_view(),name="showclassget"),
    #path('showclass',Myclass.as_view(),name="showclass"),
]