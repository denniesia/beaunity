from django.contrib.auth.views import LogoutView
from django.urls import include, path

from . import views


urlpatterns = [

    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
        path('make-superuser/', views.make_superuser, name='make-superuser'),
        path('make-moderator/', views.make_moderator, name='make-moderator'),
        path('make-organizer/', views.make_organizer, name='make-organizer'),
        path('remove-roles/', views.remove_roles, name='remove-roles'),
    ])),
    path('api/', include('beaunity.accounts.api_urls')),
]
