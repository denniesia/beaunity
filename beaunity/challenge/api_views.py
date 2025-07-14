from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from .models import Challenge
from rest_framework.permissions import IsAuthenticated
from .permissions import CanApprove
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from beaunity.challenge.serializers import ChallengeCreateSerializer
#
# class ChallengeViewSet(viewsets.ModelViewSet):
#     queryset = Challenge.objects.all()
#     serializer_class = ChallengeSerializer
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         challenge = serializer.save(created_by=user)
#
#         if user.has_perm('challenge.can_approve_challenge'):
#             challenge.is_approved = True
#             challenge.save()
#
#     def destroy(self, request, *args, **kwargs):
#         challenge = self.get_object()
#         if challenge.created_by != request.user:
#             return Response({'detail': 'You are not allowed to delete this challenge.'}, status=403)
#         return super().destroy(request, *args, **kwargs)
#
#     @action(detail=True, methods=['post'], permission_classes=[CanApprove])
#     def approve_challenge(self, request, pk=None):
#         challenge = self.get_object()
#         challenge.is_approved = True
#         challenge.save()
#         return Response({'status': 'Challenge approved'}, status=status.HTTP_200_OK)
#
#     @action(detail=True, methods=['post'], permission_classes=[CanApprove])
#     def disapprove_challenge(self, request, pk=None):
#         challenge = self.get_object()
#         challenge.is_approved = False
#         challenge.save()
#         return Response({'status': 'Challenge disapproved'}, status=status.HTTP_200_OK)

class ChallengeCreateAPIView(CreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        challenge = serializer.save(created_by=user)

        if user.has_perm('challenge.can_approve_challenge'):
            challenge.is_approved = True
            challenge.save()
