from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api_views


router = DefaultRouter()
router.register(r'categories', api_views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

]