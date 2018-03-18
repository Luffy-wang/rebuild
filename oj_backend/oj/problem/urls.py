from django.urls import path

from .views import admin


urlpatterns=[
    path("list/",admin.get,name="problemlist"),
    path("create",admin.post,name="problem"),
    path("test",admin.test,name="name"),
    path("upload",admin.UploadTestCase,name="upload"),
    path("problem_detail/<int:problem_id>",admin.problem_detail,name="problem_detail"),
    path("create_problem_list",admin.problem_create_list,name="create_problem_list"),
]