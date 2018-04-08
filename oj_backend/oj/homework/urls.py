from django.conf.urls import url
from .views.admin import HomeworkItem,ClassProblemItem

urlpatterns=[
    url(r"showhomework/?$",HomeworkItem.as_view,name="homework"),
    url(r"showclassproblem/?$",ClassProblemItem.as_view,name="classproblem"),
]