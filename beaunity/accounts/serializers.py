from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    message = serializers.CharField()


class LogoutRequestSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()


class LogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
