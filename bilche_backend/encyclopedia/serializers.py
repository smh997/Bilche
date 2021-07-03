from rest_framework import serializers

from encyclopedia.models import BasePlant


class BasePlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePlant
        fields = '__all__'
