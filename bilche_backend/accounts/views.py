from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import UserSerializer
from rest_framework.views import APIView


class UserRegistrationAPIView(CreateAPIView):

    def get_serializer_class(self):
        self.serializer_class = UserSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        request.data['username'] = request.data['email']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
