
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api_views

router = DefaultRouter()

router.register(r'post', api_views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),

]