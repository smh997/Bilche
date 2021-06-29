from django.contrib.auth import login
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

from accounts.serializers import UserSerializer, MyAuthTokenSerializer
from rest_framework.views import APIView


class MyObtainAuthToken(ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer


class UserRegistrationAPIView(CreateAPIView):

    def get_serializer_class(self):
        self.serializer_class = UserSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        request.data['username'] = request.data['email']
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token, create = Token.objects.get_or_create(user=user)
                data_response = dict()
                data_response['user'] = serializer.data
                data_response['token'] = token.key
                return Response(data_response, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        if 'username' in errors:
            errors.pop('username')
        return Response(data={'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

