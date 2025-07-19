from django.contrib.auth import authenticate, get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from beaunity.accounts.serializers import (LoginRequestSerializer,
                                           LoginResponseSerializer,
                                           LogoutRequestSerializer,
                                           LogoutResponseSerializer,
                                           UserSerializier)

UserModel = get_user_model()


class AppUserRegisterAPIView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializier
    permission_classes = [AllowAny]


@extend_schema(
    tags=["accounts"],
    summary="Login endpoint",
    description="Authenticates user with username and password and return access and refresh token.",
    request=LoginRequestSerializer,
    responses={
        200: LoginResponseSerializer,
        401: "Invalid username or password.",
    },
)
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {
                    "error": "Invalid username or password",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh_token = RefreshToken.for_user(user)

        return Response(
            {
                "refresh_token": str(refresh_token),
                "access_token": str(refresh_token.access_token),
                "message": "Successfully logged in.",
            },
            status=status.HTTP_200_OK,
        )


@extend_schema(
    tags=["accounts"],
    summary="Logout endpoint",
    description="Blacklists the refresh token",
    request=LogoutRequestSerializer,
    responses={
        200: LogoutResponseSerializer,
        400: "Invalid or expired token.",
    },
)
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        try:
            refresh_token = request.data.get("refresh_token")  # string
            token = RefreshToken(refresh_token)  # inistializing the token object
            token.blacklist()
            return Response(
                {
                    "message": "Successfully logged out.",
                },
                status=status.HTTP_200_OK,
            )
        except TokenError:
            return Response(
                {
                    "error": "Invalid or expired token.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
