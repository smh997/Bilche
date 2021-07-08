from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField
from django.template import loader
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    html_content = loader.render_to_string(template_name='email.html',
                                           context={'token': 'http://localhost:3000/forgotPassword?token=' + str(reset_password_token.key)})
    send_mail(
        # subject:
        "تغییر رمز عبور حساب بیلچه",
        # message:
        "",
        # from:
        "Bilche.tech@gmail.com",
        # to:
        [reset_password_token.user.email],
        # html
        html_message=html_content
    )


class User(AbstractUser):
    level_choices = (
        ('b', 'تازه کار'),
        ('m', 'سطح میانه'),
        ('p', 'حرفه ای')
    )
    fullname = models.CharField(max_length=100, blank=True, default='')
    level = models.CharField(max_length=1, choices=level_choices, default='b')
    profile_photo = models.ImageField(null=True, blank=True, upload_to='profile_photoes')
    phone_number = PhoneField(blank=True, null=True)
    email = models.EmailField(unique=True, error_messages={
        'unique': 'کاربری با این ایمیل وجود دارد.'
    })
    is_gardener = models.BooleanField(default=False)
    preferred_hour = models.DateTimeField(blank=True, null=True)
    _preferred_days = models.CharField(max_length=7, default='-------')

    @property
    def preferred_days(self):
        return [False] * 7


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
    city = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=50, blank=True, default='')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
