from rest_framework import serializers
from actor import models

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Actor
        fields = ['id','name', 'description', 'gender', 'birth']
        read_only_fields = ['id']


class ActorImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to actor."""

    class Meta:
        model = models.Actor
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'Falsee'}}
