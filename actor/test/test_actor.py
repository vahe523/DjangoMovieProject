from django.test import TestCase
from actor.models import Actor, GENDER
import datetime


class ActorTests(TestCase):
    """Test models."""


    def test_create_actor(self):
        """Test creating a user with an email is successful."""
        all_actor = {
        'name': 'actor',
        'description': 'des actor',
        'gender': GENDER.MALE,
        'birth': datetime.date(1997, 10, 19),
        'image': 'image'
        }

        actor = Actor.objects.create(**all_actor)

        self.assertEqual(actor.name, all_actor['name'])
        self.assertEqual(actor.description, all_actor['description'])
        self.assertEqual(actor.gender, all_actor['gender'])
        self.assertEqual(actor.birth, all_actor['birth'])
        self.assertEqual(actor.image, all_actor['image'])

