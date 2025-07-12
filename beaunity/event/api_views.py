from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from beaunity.event.serializers import EventSerializer

from .models import Event
from .permissions import CanAddEvent


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [CanAddEvent]

    def perform_create(self, serializer):
        user = self.request.user
        challenge = serializer.save(created_by=user)