from beaunity.common.permissions import IsCreator
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, GenericAPIView
from beaunity.event.serializers import EventSerializer
from rest_framework.viewsets import GenericViewSet

from .models import Event
from .permissions import CanAddEvent


class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [CanAddEvent]

    def perform_create(self, serializer):
        user = self.request.user
        event = serializer.save(created_by=user)


class EventEditDeleteView(UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsCreator]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class EventViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]