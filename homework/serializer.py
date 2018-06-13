from rest_framework import serializers
from .models import Homework_item

class ClassHomeworkSerializer(serializers.Serializer):
    class_name=serializers.CharField(max_length=20)
    homework_item=serializers.CharField(max_length=20)
    problem_id=serializers.CharField()
    problem_title=serializers.CharField(max_length=30)

class HomeworkItemSerializer(serializers.Serializer):
    class_name=serializers.CharField(max_length=20)
    homework_item=serializers.CharField(max_length=20)
    homework_item_title=serializers.CharField(max_length=30)

    def create(self,validated_data):
        return Homework_item.objects.create(**validated_data)
