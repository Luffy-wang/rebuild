from rest_framework import serializers

from .models import Problem

class ProblemSerializers(serializers.Serializer):
    _id=serializers.CharField()
    title=serializers.CharField(max_length=40,allow_blank="True")
    description=serializers.CharField()
    input_description=serializers.CharField()
    output_description=serializers.CharField()
    tag=serializers.CharField()
    time_limit=serializers.IntegerField()
    memory_limit=serializers.IntegerField()
    test_case_id=serializers.CharField()
    create_time=serializers.DateTimeField()

    def create(self,validated_data):
        return Problem.objects.create(**validated_data)
        

    
