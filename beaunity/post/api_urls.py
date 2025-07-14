
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api_views

router = DefaultRouter()

router.register(r'post', api_views.PostViewSet, basename='post')
urlpatterns = [
    path('', include(router.urls)),
    path('create/', api_views.PostCreateAPIView.as_view(), name='api-create-post'),
]