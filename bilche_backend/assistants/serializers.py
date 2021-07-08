from datetime import datetime, timedelta
from rest_framework import serializers

from accounts.models import User
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


class PlantObjectSerializer(serializers.ModelSerializer):
    activities = serializers.SerializerMethodField()
    next_activity = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        exclude = ('site',)

    def get_activities(self, plant)->list:
        activities = plant.activities.exclude(perform_time=None).order_by('-perform_time')
        recent_activities = activities[0:(min(len(activities), 3))]
        result = [{'id': activity.id, 'activity_type': activity.activity_type, 'set_time': activity.set_time,
                 'perform_time': activity.perform_time, 'deadline': activity.deadline,
                 'description': activity.description} for activity in recent_activities]
        return result

    def get_next_activity(self, plant)->dict:
        next_activity = plant.activities.filter(perform_time=None).last()
        result = {'id': next_activity.id, 'activity_type': next_activity.activity_type, 'set_time': next_activity.set_time,
                  'deadline': next_activity.deadline, 'description': next_activity.description}
        return result


class PreferredTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('preferred_hour', )
        extra_kwargs = {'preferred_hour': {'required': True}}

