
from django.urls import path, include

from . import api_views


urlpatterns = [
    path('create/', api_views.ChallengeCreateAPIView.as_view(), name='api-create-challenge' ),
    path('<int:pk>/', api_views.ChallengeEditDeleteView.as_view(), name='api-edit-challenge'),
]