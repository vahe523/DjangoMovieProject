from rest_framework import viewsets, generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from actor.models import Actor
from actor import serializers

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return permissions.IsAuthenticated.has_permission(self, request, view)
        return False

class ActorViewSet(viewsets.ModelViewSet):
    """View for manage recipe Apis."""
    serializer_class = serializers.ActorSerializer
    queryset = Actor.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser|ReadOnly]

    def get_queryset(self):
        """Retrieve actor for auth user."""
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.ActorSerializer
        elif self.action == 'upload_image':
            return serializers.ActorImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new actor"""
        serializer.save()

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to actor"""
        actor = self.get_object()
        serializer = self.get_serializer(actor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_ok)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActorSearchListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
