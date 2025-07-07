from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ChallengeOverviewView.as_view(), name='challenges'),
    path('create/', views.ChallengeCreateView.as_view(), name='challenge-create'),
    path('<int:pk>/', include([
        path('', views.ChallengeDetailsView.as_view(), name='challenge-details'),
        path('edit/', views.ChallengeEditView.as_view(), name='challenge-edit'),
        path('delete/', views.ChallengeDeleteView.as_view(), name='challenge-delete'),
    ])),
]