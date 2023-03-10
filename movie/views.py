from rest_framework import viewsets, generics, permissions, mixins, status
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from movie import serializers
from movie.models import Movie, Genre
# Create your views here.

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return permissions.IsAuthenticated.has_permission(self, request, view)
        return False

class GenreViewSet(viewsets.ModelViewSet):
    """View for genre Apis."""
    serializer_class = serializers.GenreSerializer
    queryset = Genre.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | ReadOnly]

    def get_queryset(self):
        """Retrieve recipe for auth user."""
        return self.queryset.order_by('-id')

class CreateMovieView(generics.CreateAPIView):
    serializer_class = serializers.MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | ReadOnly]

class MovieViewSet(viewsets.ModelViewSet):
    """View for genre Apis."""
    serializer_class = serializers.MovieSerializer
    queryset = Movie.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | ReadOnly]

    def get_queryset(self):
        """Retrieve recipe for auth user."""
        return self.queryset.order_by('-id')

    def perform_create(self, serializer):
        return serializer.save()

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.MovieSerializer
        elif self.action == 'upload_image':
            return serializers.MovieImageSerializer

        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to actor"""
        movie = self.get_object()
        serializer = self.get_serializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_ok)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieSearchListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]