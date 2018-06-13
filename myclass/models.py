from django.db import models
from account.models import User
# Create your models here.

class MyClassIndex(models.Model):
    class_name=models.CharField(max_length=30,unique=True)
    class_admin=models.CharField(max_length=30)
    create_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='myclassindex'

    def __str__(self):
        return self.class_name


class Myclass(models.Model):
    class_name=models.ForeignKey(MyClassIndex,on_delete=models.CASCADE)
    class_member=models.OneToOneField(User,on_delete=False,unique=True)
    is_activity=models.BooleanField(default=False)
    
    class Meta:
        db_table="myclass"

