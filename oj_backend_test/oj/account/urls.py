from django.urls import path

from . import views
app_name="account"
urlpatterns=[
	path("",views.ping,name="ping"),
	#path("<int:question_id>/",views.detail,name="detail"),
	#after modify
	path("<int:question>/",views.detail,name="index"),
	path("<int:question>/results/",views.results,name="results"),
	path("<int:question_id>/vote/",views.vote,name="vote"),
	path("index/",views.index,name="index"),
	path("judge/",views.judge,name="judge")
]