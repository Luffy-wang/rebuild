from django.db import models

# Create your models here.
class Announcement(models.Model):
    id=models.AutoField(primary_key=True)
    created_time=models.DateTimeField(auto_now_add=True)
    created_user_id=models.IntegerField()
    title = models.TextField()
    content=models.TextField()
    is_public=models.BooleanField()
    class Meta:
        db_table="Announcement"