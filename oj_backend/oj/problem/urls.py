from django.urls import path

from .views import admin


urlpatterns=[
    path("list",admin.get,name="problemlist"),
    path("create",admin.post,name="problem")
]