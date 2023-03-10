from django.test import TestCase
from movie.models import Movie, Genre
from actor.models import Actor


class MovieTests(TestCase):
    """Test models."""


    def test_create_movie(self):
        """Test creating a movie is successful."""
        all_movie = {
        'name': 'movie',
        'duration': 15,
        'year': 2005,
        'imdb': 5.2,
        }

        movie = Movie.objects.create(**all_movie)

        self.assertEqual(movie.name, all_movie['name'])
        self.assertEqual(movie.duration, all_movie['duration'])
        self.assertEqual(movie.year, all_movie['year'])
        self.assertEqual(movie.imdb, all_movie['imdb'])

    def test_create_genre(self):
        """Test creating a movie is successful."""
        all_genre = {
        'genre': 2
        }

        genre = Genre.objects.create(**all_genre)

        self.assertEqual(genre.genre, all_genre['genre'])


