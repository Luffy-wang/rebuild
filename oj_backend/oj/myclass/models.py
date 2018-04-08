from django.db import models

# Create your models here.

class Myclass(models.Model):
    class_name=models.IntegerField()
    class_admin=models.CharField(max_length=30)
    class_member=models.OneToOneField(User,on_delete=False,unique=True)
    is_activity=models.BooleanField(default=False)
    create_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="myclass"