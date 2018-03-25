from django.urls import path
from .views import admin

urlpatterns=[
    path("register",admin.register,name="register"),
    path("login",admin.mylogin,name="login"),
    path("logout",admin.mylogut,name="logout"),
    path("createclass",admin.create_class,name="createclass"),
    path("modifytype",admin.modify_user_type_to_teacher,name="modifytype"),
    path("showclassmember",admin.show_class_member,name="showclassmember"),
    path("shownotjoinclass",admin.not_join_the_class,name="showNotJoinClass"),
    path("joinclass",admin.join_the_class,name="joinclass"),
]