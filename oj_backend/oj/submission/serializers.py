from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.Serializer):
    id=serializers.CharField()
    create_time=serializers.DateTimeField()
    class_name=serializers.CharField()
    user_name=serializers.CharField()
    user_id=serializers.IntegerField()
    code=serializers.CharField()
    result=serializers.CharField()
    language=serializers.CharField()

    def create(self,validated_data):
        return Submission.objects.create(**validated_data)