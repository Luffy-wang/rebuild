from django.db import models
from problem.models import Problem

# Create your models here.
class Submission(models.Model):
    id=models.AutoField(primary_key=True,db_index=True)
    problem_id=models.CharField(max_length=30)
    create_time=models.DateTimeField(auto_now_add=True)
    class_name=models.CharField(max_length=30)
    user_id=models.CharField(max_length=20)
    homework_item=models.CharField(max_length=20)
    code=models.TextField()
    result=models.IntegerField()
    language=models.CharField(max_length=20)
    real_time=models.CharField(max_length=20)

    @property
    def problem_title(self):
        return self.problem.problem.title
    class Meta:
        db_table="Submission"
    



    