from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class User(AbstractUser):
    level_choices = (
        ('b', 'Beginner'),
        ('m', 'MiddleLevel'),
        ('p', 'Professional')
    )
    fullname = models.CharField(max_length=100, blank=True, default='')
    level = models.CharField(max_length=1, choices=level_choices, default='b')
    profile_photo = models.ImageField(null=True, blank=True, upload_to='profile_photoes')
    phone_number = PhoneField(unique=True, blank=True, null=True, error_messages={
        'unique': 'A user with this phone number already exists.'
    })
    email = models.EmailField(unique=True, blank=True, null=True)
    is_gardener = models.BooleanField(default=False)
    prefered_hour = models.DateTimeField(blank=True, null=True)
    _prefered_days = models.CharField(max_length=7, default='-------')

    @property
    def prefered_days(self):
        return [False] * 7


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=50, blank=True, default='')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
