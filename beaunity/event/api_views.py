from beaunity.common.permissions import IsCreator
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from beaunity.event.serializers import EventSerializer, EventCreateSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Event
from .permissions import CanAddEvent


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return EventCreateSerializer
        return EventSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsCreator()]
        elif self.action == 'create':
            return [IsAuthenticated(), CanAddEvent()]
        return [IsAuthenticated()]


    def perform_create(self, serializer):
        user = self.request.user
        event = serializer.save(created_by=user)

