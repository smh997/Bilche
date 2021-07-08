from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from encyclopedia.models import BasePlant, FavoritePlant
from encyclopedia.serializers import BasePlantListSerializer, BasePlantObjectSerializer, ReportToEditSerializer, \
    FavoritePlantSerializer


class SearchAPIView(ListAPIView):
    queryset = BasePlant.objects.all()
    serializer_class = BasePlantListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['toxic', 'irritant', 'life_span', 'pruning', 'fogging', 'cleaning_pot', 'cleaning_leaves']
    search_fields = ['title', 'scientific_name', 'common_names__name']

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = self.queryset
        categories = self.request.query_params.get('category')
        if categories is not None:
            categories = list(map(int, categories.split(',')))
            queryset = queryset.filter(categories__category__id__in=categories)
        levels = self.request.query_params.get('level')
        if levels is not None:
            levels = list(map(str, levels.split(',')))
            queryset = queryset.filter(level__in=levels)
        lights = self.request.query_params.get('light')
        if lights is not None:
            lights = list(map(str, lights.split(',')))
            queryset = queryset.filter(light__in=lights)
        return queryset

    category = openapi.Parameter('category', in_=openapi.IN_QUERY, type=openapi.TYPE_ARRAY,
                                 items=openapi.Items(type=openapi.TYPE_NUMBER))
    level = openapi.Parameter('level', in_=openapi.IN_QUERY, type=openapi.TYPE_ARRAY,
                              items=openapi.Items(type=openapi.TYPE_STRING))
    light = openapi.Parameter('light', in_=openapi.IN_QUERY, type=openapi.TYPE_ARRAY,
                              items=openapi.Items(type=openapi.TYPE_STRING))
    toxic = openapi.Parameter('toxic', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    irritant = openapi.Parameter('irritant', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    life_span = openapi.Parameter('life_span', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
    pruning = openapi.Parameter('pruning', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    fogging = openapi.Parameter('fogging', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    cleaning_pot = openapi.Parameter('cleaning_pot', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    cleaning_leaves = openapi.Parameter('cleaning_leaves', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)

    @swagger_auto_schema(manual_parameters=[category, level, light, toxic, irritant, life_span, pruning, fogging,
                                            cleaning_pot, cleaning_leaves])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetBasePlantAPIView(RetrieveAPIView):
    serializer_class = BasePlantObjectSerializer
    queryset = BasePlant.objects.all()
    lookup_field = 'pk'


class ReportEditPlantAPIView(CreateAPIView):
    serializer_class = ReportToEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        self.request.data['base_plant'] = self.kwargs.get('id')
        self.request.data['user'] = self.request.user.id
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class FavoritePlantAPIView(APIView):
    serializer_class = FavoritePlantSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        self.request.data['base_plant'] = self.kwargs.get('id')
        self.request.data['user'] = self.request.user.id
        serializer_class = self.serializer_class
        return serializer_class(*args, **kwargs)

    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        base_plant = BasePlant.objects.get(pk=request.data.get('base_plant'))
        like, created = FavoritePlant.objects.get_or_create(user=request.user, base_plant=base_plant)
        if not created:
            like.delete()
        else:
            like.save()
        return Response(status=status.HTTP_200_OK)



