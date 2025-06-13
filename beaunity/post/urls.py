from django.urls import path, include
from . import views
urlpatterns = [
    path('dashboard/', views.ForumDashboardView.as_view(), name='forum-dashboard' ),
    path('<int:pk>', include([
        path('', views.PostDetailsView.as_view(), name='post-details'),
    ])),


]