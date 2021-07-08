from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from accounts.models import User
from assistants.models import Site, Plant
from assistants.serializers import SiteSerializer, SitesListSerializer, SiteObjectSerializer, PlantSerializer, \
    PlantObjectSerializer, PreferredTimeSerializer


class AddNewSiteAPIView(CreateAPIView):
    serializer_class = SiteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        self.request.data['user'] = self.request.user.id
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class GetSitesAPIView(ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SitesListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class SiteAPIView(APIView):
    serializer_class = SiteObjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        queryset = Site.objects.all()
        instance = get_object_or_404(queryset, id=kwargs.get('site_id'))
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'name': openapi.Schema(type=openapi.TYPE_STRING),
                                 'type': openapi.Schema(type=openapi.TYPE_STRING),
                                 'light': openapi.Schema(type=openapi.TYPE_STRING, enum=['d', 'i', 'l', 'a']),
                                 'temperature': openapi.Schema(type=openapi.TYPE_STRING, enum=['r']),
                                 'humidity': openapi.Schema(type=openapi.TYPE_STRING, enum=['d', 'n', 'h']),
                             },))
    def put(self, request, *args, **kwargs):
        queryset = Site.objects.all()
        instance = get_object_or_404(queryset, id=kwargs.get('site_id'))
        print(request.data)
        for val in request.query_params:
            request.data[val] = request.query_params[val]
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        queryset = Site.objects.all()
        instance = get_object_or_404(queryset, id=kwargs.get('site_id'))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddNewPlantAPIView(CreateAPIView):
    serializer_class = PlantSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        self.request.data['site'] = self.kwargs.get('site_id')
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class PlantAPIView(APIView):
    serializer_class = PlantObjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        queryset = Plant.objects.all()
        instance = get_object_or_404(queryset, id=kwargs.get('plant_id'))
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        queryset = Plant.objects.all()
        instance = get_object_or_404(queryset, id=kwargs.get('plant_id'))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PreferredTimeAPIView(APIView):
    serializer_class = PreferredTimeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['preferred_hour', ],
        properties={
            'preferred_hour': openapi.Schema(type=openapi.TYPE_STRING),
        }, ))
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
