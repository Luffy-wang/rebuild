from django.db import models

from problem.models import Problem
# Create your models here.
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