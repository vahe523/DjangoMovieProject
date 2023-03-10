from rest_framework import serializers
from movie import models
from actor.serializers import ActorSerializer

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Genre
        fields = '__all__'
        raed_only_fields = ['id']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, required=False)
    actors = ActorSerializer(many=True, required=False)

    class Meta:
        model = models.Movie
        fields = ['id','name', 'duration', 'year', 'imdb', 'genres', 'actors']
        read_only_fields = ['id']



class MovieImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to actor."""

    class Meta:
        model = models.Movie
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Genre
        fields = '__all__'
        raed_only_fields = ['id']
