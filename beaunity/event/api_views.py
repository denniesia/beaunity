from beaunity.common.permissions import IsCreatorOrSuperuser
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from beaunity.event.serializers import EventSerializer, EventCreateSerializer

from .models import Event
from .permissions import CanAddEvent


class EventViewSet(ModelViewSet):
    queryset = Event.objects.order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'create':
            return EventCreateSerializer
        return EventSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsCreatorOrSuperuser()]
        elif self.action == 'create':
            return [IsAuthenticated(), CanAddEvent()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        user = self.request.user
        event = serializer.save(created_by=user)

