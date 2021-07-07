from rest_framework import serializers

from encyclopedia.models import BasePlant, ReportToEdit, FavoritePlant


class BasePlantListSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = BasePlant
        fields = ('id', 'title', 'picture')

    def get_picture(self, base_plant):
        return base_plant.pictures.first().picture.url


class BasePlantObjectSerializer(serializers.ModelSerializer):
    common_names = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    pictures = serializers.SerializerMethodField()
    waterings = serializers.SerializerMethodField()
    fertilizers = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField()

    class Meta:
        model = BasePlant
        fields = '__all__'

    def get_common_names(self, base_plant):
        return [common_name.name for common_name in base_plant.common_names.all()]

    def get_categories(self, base_plant):
        # return [category for category in (pcategory.category for pcategory in base_plant.categories.all())]
        return [category for category in base_plant.categories.values_list('category__id', 'category__name')]

    def get_pictures(self, base_plant):
        return [image.picture.url for image in base_plant.pictures.all()]

    def get_waterings(self, base_plant):
        return [watering for watering in base_plant.waterings.values_list('season', 'range')]

    def get_fertilizers(self, base_plant):
        return [fertilizer for fertilizer in base_plant.fertilizers.values_list('base_fertilizer__name', 'season', 'range')]

    def get_colors(self, base_plant):
        return [color for color in base_plant.flower_colors.values_list('flower_color__color_code', 'flower_color__color_name')]

    def get_like(self, base_plant):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            return True if FavoritePlant.objects.filter(user=request.user, base_plant=base_plant).exists() else False
        return False


class ReportToEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportToEdit
        fields = '__all__'
        extra_kwargs = {'base_plant': {'required': False}, 'user': {'required': False}}


class FavoritePlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePlant
        fields = '__all__'
        extra_kwargs = {'base_plant': {'required': False}, 'user': {'required': False}}
