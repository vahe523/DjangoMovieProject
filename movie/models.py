import os
import uuid

from django.db import models
from django_enumfield import enum
from actor import models as actor
from user import models as user
# Create your models here.

def movie_image_file_path(instance, filename):
    """Generate file path for new actor image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'movie', filename)


class GENRE(enum.Enum):
    ACTION = 0
    COMEDY = 1
    DRAMA = 2
    FANTASY = 3
    HORROR = 4
    MYSTERY = 5
    ROMANCE = 6
    THRILLER = 7
    UNKNOWNGENRE = 8


class Movie(models.Model):
    """Movie object."""
    name = models.CharField(max_length=255)
    duration = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    imdb = models.DecimalField(max_digits=2, decimal_places=1,blank=True)
    image = models.ImageField(null=True, upload_to=movie_image_file_path)
    genres = models.ManyToManyField('Genre')
    actors = models.ManyToManyField('actor.Actor')

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Genre object."""
    genre = enum.EnumField(GENRE, default=GENRE.UNKNOWNGENRE)

    def __str__(self):
        return self.genre.name

