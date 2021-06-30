from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from home_page.serializers import FeedbackSerializer, SubscribeSerializer, InstallappSerializer


class FeedbackAPIView(CreateAPIView):
    def get_serializer_class(self):
        self.serializer_class = FeedbackSerializer
        return self.serializer_class


class SubscribeAPIView(CreateAPIView):
    def get_serializer_class(self):
        self.serializer_class = SubscribeSerializer
        return self.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "ثبت نام شما در خبرنامه بیلچه با موفقیت انجام شد"}, status=status.HTTP_201_CREATED)

        return Response({'message': serializer.errors})


class InstallappAPIView(CreateAPIView):
    def get_serializer_class(self):
        self.serializer_class = InstallappSerializer
        return self.serializer_class
