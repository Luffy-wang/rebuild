from django.urls import path
from .views import admin

urlpatterns=[
    path("register",admin.register,name="register"),#need user_id, name,password
    path("login",admin.mylogin,name="login"),#need user_id,password
    path("logout",admin.mylogut,name="logout"),
    path("createclass",admin.create_class,name="createclass"),#need class_name,user_id,notice the different of teacher and student
    path("modifytype",admin.modify_user_type_to_teacher,name="modifytype"),#need teacher_id
    path("showclassmember",admin.show_class_member_or_class,name="showclassmember"),#need user_id
    path("shownotjoinclass",admin.not_join_the_class,name="showNotJoinClass"),#notice required teacher
    path("joinclass",admin.join_the_class,name="joinclass"),#notice need user_id
    path('showclassname',admin.showclassname,name="showclassname"),
]