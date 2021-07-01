from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from home_page.serializers import FeedbackSerializer, SubscribeSerializer, InstallappSerializer


class FeedbackAPIView(CreateAPIView):
    def get_serializer_class(self):
        self.serializer_class = FeedbackSerializer
        return self.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "نظر شما با موفقیت ثبت شد"},
                            status=status.HTTP_201_CREATED)
        messages = list(serializer.errors.values())[0]
        error = {'error': messages[0]}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class SubscribeAPIView(CreateAPIView):
    def get_serializer_class(self):
        self.serializer_class = SubscribeSerializer
        return self.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "ثبت نام شما در خبرنامه بیلچه با موفقیت انجام شد"}, status=status.HTTP_201_CREATED)
        messages = list(serializer.errors.values())[0]
        error = {'error': messages[0]}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class InstallappAPIView(CreateAPIView):
    def get_serializer_class(self):
        self.serializer_class = InstallappSerializer
        return self.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        messages = list(serializer.errors.values())[0]
        error = {'error': messages[0]}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
