from django.urls import path
from .views import admin


urlpatterns=[
    path("1",admin.get,name="submission_index"),
    path("post1",admin.post,name="submission"),   #create submission,required class_name ,problem_id,code and wait todo
    path("showclassproblem",admin.showClassProblem,name="showclassproblem"),#need class_name
    path("addproblemtoclass",admin.addProblemToClass,name="addProblemToClass"),#need class_name,problem_id
    path("showsamplesubmission",admin.showSampleSubmission,name="showsamplesubmission"),#need user_id
    path('createhomework',admin.createHomeworkItem,name="createhomework"),
    path('showhomeworkitem',admin.showHomeworkItem,name='showhomeworkitem'),
    path("testuserobject",admin.testuserobject,name="testuserobjects"),
]