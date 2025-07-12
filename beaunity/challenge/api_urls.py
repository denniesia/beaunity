from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .api_views import ChallengeViewSet

router = DefaultRouter()
router.register(r'api/challenges', ChallengeViewSet)

urlpatterns = [
    path('', include(router.urls)),

]