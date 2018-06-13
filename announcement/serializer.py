from rest_framework import serializers

class AnnouncementSerializer(serializers.Serializer):
    title=serializers.CharField()
    content=serializers.CharField()
    is_public = serializers.CharField()

