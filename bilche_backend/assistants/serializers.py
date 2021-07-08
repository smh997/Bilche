from datetime import datetime, timedelta
from rest_framework import serializers

from assistants.models import Site, Plant, Activity


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}


class SitesListSerializer(serializers.ModelSerializer):
    plants_pictures = serializers.SerializerMethodField()

    class Meta:
        model = Site
        exclude = ('user',)

    def get_plants_pictures(self, site)->list:
        return [plant.base_plant.pictures.first().picture.url for plant in site.plants.all()]


class SiteObjectSerializer(serializers.ModelSerializer):
    plants = serializers.SerializerMethodField()

    class Meta:
        model = Site
        exclude = ('user',)

    def get_plants(self, site)->list:
        return [{'id': plant.id, 'name': plant.name, 'picture': plant.base_plant.pictures.first().picture.url,
                 'base_plant_id': plant.base_plant.id, 'base_plant_title': plant.base_plant.title}
                for plant in site.plants.all()]


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        exclude = ('is_alive', )
        extra_kwargs = {'site': {'required': False}}

    def create(self, validated_data):
        plant = Plant.objects.create(**validated_data)
        now = datetime.now()
        deadline = now + timedelta(days=plant.base_plant.waterings.first().range)
        activity = Activity.objects.create(plant=plant, activity_type='w', set_time=now, deadline=deadline,
                                           description='اولین آبیاری:)')
        return plant
