from django.urls import path
from .views import admin

urlpatterns=[
    path("register",admin.get,name="get"),
    path("api_register",admin.register,name="register"),
    path("mylogin",admin.mylogin,name="login"),
    path("login",admin.mylogin_index,name="login_index"),
    path("logout",admin.my_logut,name="logout"),
    path("index",admin.index,name="index"),
]