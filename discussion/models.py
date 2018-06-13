from django.db import models
from account.models import User
from problem.models import Problem


class Discussion(models.Model):
    id=models.AutoField(primary_key=True)
    created_time=models.DateTimeField(auto_now_add=True)
    created_user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    problem_id=models.ForeignKey(Problem,on_delete=models.CASCADE)
    class Meta:
        db_table="Discussion"

class DiscussionFollow(models.Model):
    id=models.AutoField(primary_key=True)
    discussion=models.ForeignKey(Discussion,on_delete=models.CASCADE)
    follow_user=models.ManyToManyField(User)
    content=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="DiscussionFollow"