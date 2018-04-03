from django.db import models
from problem.models import Problem

# Create your models here.
class Submission(models.Model):
    id=models.AutoField(primary_key=True,db_index=True)
    #problem=models.ForeignKey(Problem,on_delete=True)
    problem_id=models.CharField(max_length=30)
    create_time=models.DateTimeField(auto_now_add=True)
    class_name=models.CharField(max_length=30)
    user_id=models.CharField(max_length=20)
    homework_item=models.CharField(max_length=20)
    #user_name=models.CharField(max_length=30)
    code=models.TextField()
    result=models.IntegerField()
    language=models.CharField(max_length=20)

    @property
    def problem_title(self):
        return self.problem.problem.title
    class Meta:
        db_table="Submission"
    
class Homework_item(models.Model):
    class_name=models.CharField(max_length=20)
    homework_item=models.CharField(max_length=20)
    homework_item_title=models.CharField(max_length=30)

class ClassHomework(models.Model):
    class_name=models.CharField(max_length=20)
    homework_item=models.ForeignKey(Homework_item,on_delete=models.CASCADE,related_name="homework")
    problem_id=models.ForeignKey(Problem,on_delete=models.CASCADE)
    problem_title=models.CharField(max_length=30,default="a")


    @property
    def problem_real_id(self):
        return self.problem_id._id


    