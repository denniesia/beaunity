from django.urls import path
from . import api_views

urlpatterns = [
    path('search/', api_views.global_search, name='api-global-search' ),
]