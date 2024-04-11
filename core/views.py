from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import generics, serializers, status
from drf_spectacular.utils import extend_schema

from .serializers import UserSerializer, MessageSerializer, ResponseSerializer
from .tools_utils import *

class UserDirectRegistrationView(generics.GenericAPIView):
    serializer_class = UserSerializer

    @extend_schema(
        request=UserSerializer,
        responses={204: None},
        methods=["POST"]
    )
    def post(self, request):
        user = get_object_or_404(User, username=request.data.get('username'))
        if not user.check_password(request.data.get('password')):
            return Response("Invalid credentials", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})


class LoginView(APIView):
    @extend_schema(
        request=UserSerializer,
        responses={200: UserSerializer}
    )
    def post(self, request):
        user = get_object_or_404(User, username=request.data.get('username'))
        if not user.check_password(request.data.get('password')):
            return Response("Invalid credentials", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})


class SignupView(APIView):
    @extend_schema(
        request=UserSerializer,
        responses={200: UserSerializer}
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestTokenView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"passed for {}".format(request.user.username)})


class ChatWith_qwen_72b(APIView):
    serializer_class = MessageSerializer
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    @extend_schema(
        request=MessageSerializer,
        responses={200: ResponseSerializer}
    )
    def post(self, request):
        message = request.data['message']
        print(message)
        response = call_qwen1572_client(message)
        return Response({
            "response": response
        }, status=status.HTTP_200_OK)


class ChatWith_gpt_3_5(APIView):
    serializer_class = MessageSerializer
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    @extend_schema(
        request=MessageSerializer,
        responses={200: ResponseSerializer}
    )
    def post(self, request):
        message = request.data['message']
        print(message)
        response = call_with_gpt_3_5(message)
        return Response({
            "response": response
        }, status=status.HTTP_200_OK)


class ChatWith_claude_3_opus(APIView):
    serializer_class = MessageSerializer
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    @extend_schema(
        request=MessageSerializer,
        responses={200: ResponseSerializer}
    )
    def post(self, request):
        message = request.data['message']
        print(message)
        response = call_with_claude_3_opus(message)
        return Response({
            "response": response
        }, status=status.HTTP_200_OK)


