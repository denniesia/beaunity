
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views
router = DefaultRouter()
router.register(r'challenges', api_views.ChallengeViewSet, basename='challenge')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', api_views.ChallengeCreateAPIView.as_view(), name='api-create-challenge' ),
    path('<int:pk>/', api_views.ChallengeEditDeleteView.as_view(), name='api-edit-challenge'),
]