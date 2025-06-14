from django.urls import path, include
from . import views
urlpatterns = [
    path('dashboard/', views.ForumDashboardView.as_view(), name='forum-dashboard' ),
    path('<int:pk>/', include([
        path('', views.PostDetailsView.as_view(), name='post-details'),
        path('edit/', views.PostEditView.as_view(), name='post-edit'),
        path('delete/', views.PostDeleteView.as_view(), name='post-delete'),
    ])),
    path('pending/', views.PendingPostsView.as_view(), name='post-pending'),


]