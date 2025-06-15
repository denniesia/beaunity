from django.urls import path
from . import views
from .views import not_found_page

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bad-exit/', not_found_page, name='bad-exit'),
]
