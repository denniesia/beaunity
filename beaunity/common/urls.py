from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='landing-page'),
    path('about/', views.about_view, name='about'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('api/', include('beaunity.common.api_urls')),
]
handler403 = views.custom_permission_denied_view