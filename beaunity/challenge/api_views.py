from rest_framework import permissions, status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from beaunity.challenge.serializers import (ChallengeCreateSerializer,
                                            ChallengeSerializer)
from beaunity.common.permissions import IsCreator

from .models import Challenge
from .permissions import CanApprove


class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.filter(
        is_approved=True
    ).order_by('-created_at')


    def get_serializer_class(self):
        if self.action == "create":
            return ChallengeCreateSerializer
        return ChallengeSerializer

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsCreator()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        user = self.request.user
        challenge = serializer.save(created_by=user)

        if user.has_perm("challenge.can_post_without_approval"):
            challenge.is_approved = True
            challenge.save()
