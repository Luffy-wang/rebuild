from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.Serializer):
    problem_id=serializers.CharField()
    create_time=serializers.DateTimeField()
    class_name=serializers.CharField()
    homework_item=serializers.CharField()
    user_id=serializers.CharField()
    code=serializers.CharField()
    result=serializers.CharField()
    language=serializers.CharField()
    real_time=serializers.CharField()

    def create(self,validated_data):
        return Submission.objects.create(**validated_data)

    
    

