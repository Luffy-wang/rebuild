from rest_framework import serializers

from .models import Problem

class ProblemSerializers(serializers.Serializer):
    _id=serializers.CharField()
    title=serializers.CharField(max_length=40,allow_blank="True")
    description=serializers.CharField()
    input_description=serializers.CharField()
    output_description=serializers.CharField()
    simple_input=serializers.CharField()
    simple_output=serializers.CharField()
    tag=serializers.CharField()
    time_limit=serializers.IntegerField()
    memory_limit=serializers.IntegerField()
    test_case_id=serializers.CharField()
    #create_time=serializers.DateTimeField()

    def create(self,validated_data):
        return Problem.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.input_description=validated_data.get('input_description',instance.input_description)
        instance.output_description=validated_data.get('output_description',instance.output_description)
        instance.simple_input=validated_data.get('simple_input',instance.simple_input)
        instance.simple_output=validated_data.get('simple_output',instance.simple_output)
        instance.time_limit=validated_data.get('time_limit',instance.time_limit)
        instance.memory_limit=validated_data.get('memory_limit',instance.memory_limit)
        instance.tag=validated_data.get('tag',instance.tag)
        instance.save()
        return instance
        

    
