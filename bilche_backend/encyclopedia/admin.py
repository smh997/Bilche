from django.contrib import admin

from encyclopedia.models import *

admin.site.register(BasePlant)
admin.site.register(CommonName)
admin.site.register(Category)
admin.site.register(PlantCategory)
admin.site.register(Color)
admin.site.register(PlantFlowerColor)
admin.site.register(PlantLeafColor)
admin.site.register(PlantWatering)
admin.site.register(BaseFertilizer)
admin.site.register(PlantFertilizer)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Content)
admin.site.register(BasePlantTag)
admin.site.register(ContentTag)
admin.site.register(ReportToEdit)
admin.site.register(FavoritePlant)