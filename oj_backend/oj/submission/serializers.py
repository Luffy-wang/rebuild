from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.Serializer):
    problem_id=serializers.IntegerField()
    #create_time=serializers.DateTimeField(auto_now_add=True)
    class_name=serializers.CharField()
    #user_name=serializers.CharField()
    user_id=serializers.IntegerField()
    code=serializers.CharField()
    result=serializers.CharField()
    language=serializers.CharField()

    def create(self,validated_data):
        return Submission.objects.create(**validated_data)

class ClassHomeworkSerializer(serializers.Serializer):
    class_name=serializers.CharField(max_length=20)
    problem_id=serializers.CharField()
    problem_title=serializers.CharField(max_length=30)
    
    

