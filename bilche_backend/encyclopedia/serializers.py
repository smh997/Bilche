from rest_framework import serializers

from encyclopedia.models import BasePlant


class BasePlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePlant
        fields = ('title', 'scientific_name', 'family', 'level', 'need_to_check', 'fogging', 'pruning',
                  'cleaning_leaves', 'cleaning_pot', 'light', 'temperature', 'humidity', 'soil_type', 'toxic',
                  'irritant', 'life_span', 'flower_time', 'leaf_time', 'max_height', 'max_width', 'flower_type',
                  'leaf_type', 'change_pot', 'pot_type')
