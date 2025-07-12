from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import ChallengeViewSet

router = DefaultRouter()
router.register(r"challenges", ChallengeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
