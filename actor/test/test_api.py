import datetime

from django.test import TestCase
from actor import models, serializers
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

ACTORS_URL = 'http://127.0.0.1:8000/api/actor/actors/'

def create_actor(**params):
    defaults = {
        'name': 'actor name',
        'description': 'about actor',
        'gender': models.GENDER.UNKNOWNGENDER,
        'birth': datetime.date(2001,2,1),
    }
    defaults.update(params)

    actor = models.Actor.objects.create(**defaults)
    return actor


class PublicActoreApiTests(TestCase):
    """Test unauthenticated Api request"""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call Api."""
        res = self.client.get(ACTORS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateActorApiTests(TestCase):
    """Test auth Api requests."""

    def setUp(self):
        self.client = APIClient()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'string',
        )
        self.client.force_authenticate(self.user)


    def test_retrive_actors(self):
        """Test retrive actor"""
        create_actor()
        create_actor()

        res = self.client.get(ACTORS_URL)

        actors = models.Actor.objects.all().order_by('-id')
        serializer = serializers.ActorSerializer(actors, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_actor(self):
        """Test create actor."""
        payload = {
            'name': 'actor',
            'description': 'description',
            'gender': models.GENDER.MALE.value,
            'birth': datetime.date(1997, 10, 19)
        }

        res = self.client.post(ACTORS_URL, payload)

        self.assertNotEqual(res.status_code, status.HTTP_201_CREATED)

        self.client.force_authenticate(self.admin_user)
        res_admin = self.client.post(ACTORS_URL, payload)


        self.assertEqual(res_admin.status_code, status.HTTP_201_CREATED)

        actor = models.Actor.objects.get(id=res_admin.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(actor, k), v)

