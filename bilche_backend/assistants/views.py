from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from assistants.models import Site
from assistants.serializers import SiteSerializer, SitesListSerializer, SiteObjectSerializer


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
        instance = get_object_or_404(queryset, id=kwargs.get('pk'))
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

