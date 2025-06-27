from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='landing-page'),
    path('search/', views.SearchView.as_view(), name='search'),
]
handler403 = views.custom_permission_denied_view