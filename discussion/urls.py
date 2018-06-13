from django.urls import path
from .views.admin import discussion

urlpatterns=[
    path("discussionAddPage/<int:problem_id>/", discussion.addpage, name="discussion_addPage"),
    path("discussionAdmin/", discussion.as_view(), name="discussion_admin"),
]