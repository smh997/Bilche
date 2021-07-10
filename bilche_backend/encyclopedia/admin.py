from django.contrib import admin

from encyclopedia.models import *


class CategoryInline(admin.StackedInline):
    model = PlantCategory
    extra = 0


class CommonNameTabularInline(admin.TabularInline):
    model = CommonName
    extra = 0


class PlantWateringTabularInline(admin.TabularInline):
    model = PlantWatering
    extra = 0


@admin.register(BasePlant)
class BasePlantAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identity', {
            'fields': (
                'title',
                'scientific_name',
                'family'
            )
        }),
        ('Hardship & Check', {
            'fields': (
                'level',
                'need_to_check',
                'fogging',
                'pruning',
                'cleaning_leaves',
                'cleaning_pot'
            )
        }),
        ('Environment', {
            'fields': (
                'light',
                'temperature',
                'humidity',
                'soil_type',
                'pot_type'
            ),
        }),
        ('Vital Properties', {
            'fields': (
                'toxic',
                'irritant',
            )
        }),
        ('life & Growth', {
            'fields': (
                'life_span',
                'flower_time',
                'leaf_time',
                'max_height',
                'max_width'
            )
        }),
        ('Others', {
            'fields': (
                'flower_type',
                'leaf_type'
            )
        })
    )

    list_display = (
        'id',
        'title',
        'family',
        'level',
        'temperature',
        'humidity',
        'toxic'
    )

    search_fields = (
        'title',
        'scientific_name'
    )
    list_filter = (
        'family',
        'level',
        'need_to_check',
        'light',
        'temperature',
        'humidity',
        'soil_type',
        'pot_type',
        'toxic',
        'irritant'
    )
    inlines = (CategoryInline, CommonNameTabularInline, PlantWateringTabularInline)


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