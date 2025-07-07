from django.urls import path, include
from . import views
from .views import  post_confirmation

urlpatterns = [
    path('dashboard/', views.ForumDashboardView.as_view(), name='forum-dashboard' ),
    path('create', views.PostCreateView.as_view(), name='post-create'),
    path('create/confirmation', post_confirmation, name='post-confirmation'),
    path('<int:pk>/', include([
        path('', views.PostDetailsView.as_view(), name='post-details'),
        path('edit/', views.PostEditView.as_view(), name='post-edit'),
        path('delete/', views.PostDeleteView.as_view(), name='post-delete'),
        path('approve/', views.approve_post, name='post-approve'),
        path('disapprove/', views.disapprove_post , name='post-disapprove'),
    ])),
    path('pending/', views.PendingPostsView.as_view(), name='post-pending'),
    # path('search/', forum_search, name='post-search'),


]