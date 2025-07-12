from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions
from .models import Challenge
from rest_framework.permissions import IsAuthenticated

from beaunity.challenge.serializers import ChallengeSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        challenge = serializer.save(created_by=user)

        if user.has_perm('challenge.can_approve_challenge'):
            challenge.is_approved = True
            challenge.save()

