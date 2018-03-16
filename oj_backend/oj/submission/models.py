from django.db import models
from problem.models import Problem
from 
# Create your models here.
class Submission(models.Model):
    id=models.CharField(max_length=32,primary_key=True,db_index=True)
    problem=models.Foreignkey(Problem)
    create_time=models.DateTimeField(auto_now_add=True)
    class_name=models.CharField(max_length=30)
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=30)
    code=models.TextField()
    result=models.IntegerField()
    language=models.CharField(max_length=20)

    class Meta:
        db_table="Submission"
        ordering=("-create_time")