# from rest_framework import serializers
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta(object):
#         model = User
#         fields = ['id', 'username', 'password', 'email']

from rest_framework import serializers
from django.contrib.auth.models import User

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