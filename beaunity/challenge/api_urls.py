from beaunity.challenge.api_views import ChallengeCreateAPIView
from django.urls import path, include

from . import api_views


urlpatterns = [
    path('create/', ChallengeCreateAPIView.as_view(), name='api-create-challenge' ),

]