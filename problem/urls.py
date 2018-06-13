from django.urls import path
from django.conf.urls import url
from .views.admin import ProblemClass,ProblemDetail,UploadTestCase#,Problemindex,Index



urlpatterns=[
    url(r"^showclass/?$",ProblemClass.as_view(),name="showclass"),
    url(r"^problemdetail/?$",ProblemDetail.as_view(),name="problemdetail"),
    url(r"^uploadtestcase/?$",UploadTestCase.as_view(),name="uploadTestcase"),
    #url(r"^index/?$",Problemindex.as_view(),name="index"),
    #url(r"acc/?$",Index.as_view(),name='acc'),
]