from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions
from .models import Challenge
from rest_framework.permissions import IsAuthenticated
from .permissions import CanApprove

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

    @action(detail=True, methods=['post'], permission_classes=[CanApprove])
    def approve(self, request, pk=None):
        challenge = self.get_object()
        challenge.is_approved = True
        challenge.save()
        return Response({'status': 'Challenge approved'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[CanApprove])
    def disapprove(self, request, pk=None):
        challenge = self.get_object()
        challenge.is_approved = False
        challenge.save()
        return Response({'status': 'Challenge disapproved'}, status=status.HTTP_200_OK)