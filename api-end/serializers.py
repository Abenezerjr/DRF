from rest_framework import serializers


class MovieSeralizer(serializers.Serializer):
    id = serializers.Serializer(read_only=True)
    name=serializers.CharField(max_length=50)
    description=serializers.CharField(max_length=200)
    active=serializers.BooleanField()