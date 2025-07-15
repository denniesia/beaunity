from beaunity.common.permissions import IsCreator
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions
from rest_framework.viewsets import  ModelViewSet
from .models import Challenge
from rest_framework.permissions import IsAuthenticated
from .permissions import CanApprove

from rest_framework.response import Response
from rest_framework import status
from beaunity.challenge.serializers import ChallengeSerializer, ChallengeCreateSerializer


class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return ChallengeCreateSerializer
        return ChallengeSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsCreator()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        user = self.request.user
        challenge = serializer.save(created_by=user)

        if user.has_perm('challenge.can_post_without_approval'):
            challenge.is_approved = True
            challenge.save()


