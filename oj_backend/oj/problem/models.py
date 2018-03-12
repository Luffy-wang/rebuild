from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.
class ProblemTag(models.Model):
    name=models.CharField(max_length=10)
    class Meta:
        db_table="problem_tag" # db_table used to override the database table name
    
#class ProblemRuleType(Choices):
#    exercise="exericise"
#    exam="exam"

class ProblemLevel(object):
    low="low"
    medium="medium"
    high="high"

class Problem(models.Model):
    _id=models.CharField(max_length=24,db_index=True)
    title=models.CharField(max_legthn=30)
    
    exam=models.ForeignKey(null=True,blank=True)#todo import exercise
    description=CharField(max_length=50)
    input_description=CharField(max_length=50)
    output_description=CharField(max_length=50)
    
    test_case_id=models.CharField(max_length=10) #todo
    tag=models.CharField(max_leghth=20)
    languages=JSONField()#todo detele
    create_time=models.DateTimeField(auto_now_add=True)
    last_update_time=models.DateTimeField(blank=True,null=True)
    created_by=models.ForeignKey(User)  #todo import usr
    #ms
    time_limit=models.IntegerField()
    memory_limit=models.IntegerField()