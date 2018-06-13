from rest_framework import serializers
from .models import Myclass


class ShowClassSerializer(serializers.Serializer):
    class_name=serializers.CharField(max_length=30)
    class_admin=serializers.CharField(max_length=30)
    create_time=serializers.DateTimeField()


class MyclassSerializer(serializers.Serializer):
    class_name=serializers.CharField(max_length=30)
    
    class_member=serializers.CharField(max_length=30)