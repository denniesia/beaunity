from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api_views

router = DefaultRouter()

router.register(r"events", api_views.EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('create/', api_views.EventCreateAPIView.as_view(), name='api-create-event'),
    path('<int:pk>/', api_views.EventEditDeleteView.as_view(), name='api-edit-event'),
]
