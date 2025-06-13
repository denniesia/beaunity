from django.urls import path, include
from . import views
urlpatterns = [
    path('dashboard/', views.ForumDashboardView.as_view(), name='forum-dashboard' ),

]