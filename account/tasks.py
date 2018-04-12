from __future__ import absolute_import, unicode_literals
from celery import shared_task
from account.models import User

@shared_task
def butch_create(*,user_id,user_name,password):
    User.objects.create_user(user_id=user_id,user_name=user_name,password=password)
    