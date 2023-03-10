from django.test import TestCase
from movie import models, serializers
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status

MOVIES_URL = 'http://127.0.0.1:8000/api/movie/movies/'
GENRES_URL = 'http://127.0.0.1:8000/api/movie/genres/'


class PublicMoviesApiTests(TestCase):
    """Test unauthenticated Api request"""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call Api."""
        res_movies = self.client.get(MOVIES_URL)
        self.assertEqual(res_movies.status_code, status.HTTP_401_UNAUTHORIZED)

        res_genres = self.client.get(GENRES_URL)
        self.assertEqual(res_genres.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateMovieApiTests(TestCase):
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


    def test_create_movie(self):
        """Test create actor."""
        payload = {
            'name': 'movie',
            'duration': 15,
            'year': 2005,
            'imdb': 6
        }

        res = self.client.post(MOVIES_URL, payload)

        self.assertNotEqual(res.status_code, status.HTTP_201_CREATED)

        self.client.force_authenticate(self.admin_user)
        res_admin = self.client.post(MOVIES_URL, payload)

        self.assertEqual(res_admin.status_code, status.HTTP_201_CREATED)

        movie = models.Movie.objects.get(id=res_admin.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(movie, k), v)

    def test_create_genre(self):
        """Test create actor."""
        payload = {
            'genre': 1
        }

        res = self.client.post(GENRES_URL, payload)

        self.assertNotEqual(res.status_code, status.HTTP_201_CREATED)

        self.client.force_authenticate(self.admin_user)
        res_admin = self.client.post(GENRES_URL, payload)

        self.assertEqual(res_admin.status_code, status.HTTP_201_CREATED)

        movie = models.Genre.objects.get(id=res_admin.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(movie, k), v)


