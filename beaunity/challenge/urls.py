from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ChallengeOverviewView.as_view(), name='challenges'),
    path('create/', views.ChallengeCreateView.as_view(), name='challenge-create'),
    path('create/confirmation/', views.challenge_confirmation, name='challenge-confirmation'),
    path('<int:pk>/', include([
        path('', views.ChallengeDetailsView.as_view(), name='challenge-details'),
        path('edit/', views.ChallengeEditView.as_view(), name='challenge-edit'),
        path('delete/', views.ChallengeDeleteView.as_view(), name='challenge-delete'),
        path('approve/', views.approve_challenge, name='challenge-approve'),
        path('disapprove/', views.disapprove_challenge, name='challenge-disapprove'),
    ])),
    path('pending/', views.PendingChallengeView.as_view(), name='challenge-pending'),
]