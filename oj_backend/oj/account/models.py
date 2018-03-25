from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class User_type(object):
    ADMIN="Admin"
    TEACHER="Teacher"
    STUDENT="Student"


class MyUserManager(BaseUserManager):
    def create_user(self, user_id, user_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_id and user_name:
            raise ValueError('Users must have an student_id and username')

        user=self.model(user_id=user_id,user_name=user_name,password=None)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user=self.create_user(user_id=user_id,user_name=user_name,password=password)
        
        user.user_admin=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
   
    user_id=models.CharField(primary_key=True,max_length=20,unique=True)
    user_name=models.CharField(max_length=10,null=True)
    create_time=models.DateTimeField(auto_now_add=True,null=True)
    email=models.EmailField(null=True)
    user_type=models.CharField(max_length=32,default=User_type.STUDENT)

    objects = MyUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_name']

    def is_admin(self):
        return self.user_type==User_type.ADMIN

    def is_teacher(self):
        return self.user_type==User_type.TEACHER

    def is_student(self):
        return self.user_type==User_type.STUDENT

    # def returnid(self):
    #    return self.id 
    def __str__(self):
        return self.user_id


class Myclass(models.Model):
    class_name=models.CharField(max_length=30)
    class_admin=models.CharField(max_length=30)
    class_member=models.OneToOneField(User,on_delete=False,unique=True)
    is_activity=models.BooleanField(default=False)
    create_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="myclass"