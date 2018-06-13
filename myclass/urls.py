from django.urls import path
from django.conf.urls import url
from .views.admin import Mycclass,classMemeber,classApply


urlpatterns=[
    url(r"^showclass/?$",Mycclass.as_view(),name="showclassget"),
    url(r"^classmember/?$",classMemeber.as_view(),name='classmember'),
    url(r"^applyclass/?$",classApply.as_view(),name="apply"),
]