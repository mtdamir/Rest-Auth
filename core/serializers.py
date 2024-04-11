from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {
            'password': {'write_only': True},  # Password field is write-only
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField()

    class Meta:
        model = User
        fields = ('message',)


class ResponseSerializer(serializers.ModelSerializer):
    response = serializers.CharField()

    class Meta:
        model = User
        fields = ('response',)
