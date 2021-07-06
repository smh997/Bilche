from django.db import models

from accounts.models import User
from encyclopedia.models import BasePlant


class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sites')
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    light_choices = (
        ('d', 'مستقیم'),
        ('i', 'غیر مستقیم'),
        ('l', 'کم‌نور'),
        ('a', 'نور مصنوعی')
    )
    light = models.CharField(max_length=1, choices=light_choices)
    temperature_choices = (
        ('r', 'دمای اتاق'),
    )
    temperature = models.CharField(max_length=1, choices=temperature_choices)
    humidity_choices = (
        ('d', 'خشک'),
        ('n', 'معمولی'),
        ('h', 'مرطوب')
    )
    humidity = models.CharField(max_length=1, choices=humidity_choices)


class Plant(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='plants')
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='plant_instances')
    name = models.CharField(max_length=50)
    soil_type_choices = (
        ('w', 'آب'),
        ('l', 'خاک سبک'),
        ('c', 'خاک مخلوط')
    )
    soil_type = models.CharField(max_length=1, choices=soil_type_choices)
    is_alive = models.BooleanField(default=True)


class Activity(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='activities')
    activity_type_choices = (
        ('w', 'آبیاری'),
    )
    activity_type = models.CharField(max_length=1, choices=activity_type_choices)
    set_time = models.DateTimeField()
    perform_time = models.DateTimeField(null=True)
    deadline = models.DateTimeField()
    description = models.TextField()
