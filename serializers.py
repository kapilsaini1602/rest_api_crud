from .models import *
from rest_framework import serializers


class recordSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    designation = serializers.CharField(max_length=30)
    contact = serializers.IntegerField()

    def create(self, validated_data):
        return record.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()
        return instance
