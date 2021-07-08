from django.db import models
from phone_field import PhoneField

from accounts.models import User


class BilcheFeedback(models.Model):
    fullname = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField()
    text = models.TextField()


class BilcheSubscribe(models.Model):
    email = models.EmailField(null=True)
    phone_number = PhoneField(null=True)


class BilcheInstallapp(models.Model):
    application_store_choices = (
        ('sa', 'Sib app'),
        ('s', 'Sibche'),
        ('b', 'Bazaar'),
        ('g', 'Google play'),
        ('d', 'Direct')
    )
    application_store = models.CharField(max_length=2, choices=application_store_choices)

