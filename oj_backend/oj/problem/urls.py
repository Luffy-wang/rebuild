from django.urls import path

from .views import admin


urlpatterns=[
    path("list",admin.get,name="problemlist"),#show all the problem
    path("create",admin.post,name="problem"),#create problem need _id(problem_id),tag,title,description of three ,time_limit,memory_limit,test_case_id
    #path("test",admin.test,name="name"),
    path("upload",admin.UploadTestCase,name="upload"),#upload test_case,need _id(problem_id),test_case_id equal problem_id
    path("problemdetail",admin.problem_detail,name="problem_detail"),#show problem_detail need problem_id,class_name not use but need
   # path("create_problem_list",admin.problem_create_list,name="create_problem_list"),
]