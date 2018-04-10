from rest_framework import serializers
from .models import Myclass


class ShowClassSerializer(serializers.Serializer):
    class_name=serializers.CharField(max_length=30)


class MyclassSerializer(serializers.Serializer):
    class_name=serializers.CharField(max_length=30)
    class_admin=serializers.CharField(max_length=30)
    class_member=serializers.CharField(max_length=30)
    is_activity=serializers.BooleanField(default=False)
    create_time=serializers.DateTimeField()

    def create(self,validated_data):
        return Myclass.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.class_name=validated_data.get("class_name",instance.class_name)
        instance.class_admin=validated_data.get("class_admin",instance.class_admin)
        instance.is_activity=validated_data.get("is_activity",instance.is_activity)
        instance.save()
        return instance