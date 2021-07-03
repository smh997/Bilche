from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from encyclopedia.models import BasePlant, PlantCategory
from encyclopedia.serializers import BasePlantSerializer


class SearchAPIView(ListAPIView):
    queryset = BasePlant.objects.all()
    serializer_class = BasePlantSerializer
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
                                 items=openapi.Items(type=openapi.TYPE_INTEGER))
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

