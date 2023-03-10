from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from movie import views

router = DefaultRouter()
router.register('movies',views.MovieViewSet)
router.register('genres', views.GenreViewSet)

app_name = 'movies'

urlpatterns = [
    path('', include(router.urls)),
    path('movie_search', views.MovieSearchListView.as_view(), name='movie-search'),
]