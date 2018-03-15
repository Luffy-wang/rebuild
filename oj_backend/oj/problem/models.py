from django.db import models

from django.contrib.postgres.fields import JSONField
# Create your models here.
class ProblemTag(models.Model):
    name=models.CharField(max_length=10)
    class Meta:
        db_table="problem_tag" # db_table used to override the database table name

class Problem(models.Model):
    _id=models.CharField(max_length=24,db_index=True)
    title=models.CharField(max_length=30,null=True)
    
    #exam=models.ForeignKey(null=True,blank=True)#todo import exercise
    description=models.CharField(max_length=50,null=True)
    input_description=models.CharField(max_length=50,null=True)
    output_description=models.CharField(max_length=50,null=True)
    
    test_case_id=models.CharField(max_length=10,null=True) #todo
    tag=models.CharField(max_length=20,null=True)
    #languages=JSONField()#todo detele
    create_time=models.DateTimeField(auto_now_add=True,null=True)
    last_update_time=models.DateTimeField(blank=True,null=True)
    #created_by=models.ForeignKey(User)  #todo import usr
    #ms
    time_limit=models.IntegerField(null=True)
    memory_limit=models.IntegerField(null=True)