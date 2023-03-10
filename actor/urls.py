from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from actor import views

router = DefaultRouter()
router.register('actors',views.ActorViewSet)

app_name = 'actors'

urlpatterns = [
    path('', include(router.urls)),
    path('actor_search', views.ActorSearchListView.as_view(), name='actor-search'),
]