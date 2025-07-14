from beaunity.common.permissions import IsCreator
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Challenge
from rest_framework.permissions import IsAuthenticated
from .permissions import CanApprove
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from beaunity.challenge.serializers import ChallengeSerializer

class ChallengeCreateAPIView(CreateAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        challenge = serializer.save(created_by=user)

        if user.has_perm('challenge.can_approve_challenge'):
            challenge.is_approved = True
            challenge.save()

class ChallengeEditDeleteView(UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsCreator]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ChallengeViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]