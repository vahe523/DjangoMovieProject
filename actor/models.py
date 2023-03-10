import os
import uuid

from django.db import models
from django_enumfield import enum

def actor_image_file_path(instance, filename):
    """Generate file path for new actor image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'actor', filename)


class GENDER(enum.Enum):
    MALE = 0
    FEMALE = 1
    UNKNOWNGENDER = 2

class Actor(models.Model):
    """Actor object."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    gender = enum.EnumField(GENDER, default=GENDER.UNKNOWNGENDER)
    birth = models.DateField()
    image = models.ImageField(null=True, upload_to=actor_image_file_path)

    def __str__(self):
        return self.name