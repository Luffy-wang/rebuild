from django.urls import path
from .views.admin import announcement

urlpatterns=[
    path("announcementAddPage", announcement.addpage, name="announcement_addPage"),
    path("announcementUpdate/<int:id>/", announcement.updateannouncement, name="announcement_update"),
    path("announcementAdmin/", announcement.as_view(), name="announcement_admin"),
    path("announcementDelete/<int:id>/",announcement.delete,name="announcement_delete")
]