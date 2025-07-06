from django.urls import path
from . import views
urlpatterns = [
    path('', views.ChallengeOverviewView.as_view(), name='challenges'),
    path('create/', views.ChallengeCreateView.as_view(), name='challenge-create'),
]