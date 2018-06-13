from django.conf.urls import url
from .views.admin import HomeworkItem,ClassProblemItem,HomeworkIndex,HomeworkList

urlpatterns=[
    url(r"^showhomework/?$",HomeworkItem.as_view(),name="homework"),
    url(r"^showclassproblem/?$",ClassProblemItem.as_view(),name="classproblem"),
    url(r"^index",HomeworkIndex.as_view(),name='index'),
    url(r"^homeworklist",HomeworkList.as_view()),
]