import re
import django.contrib.auth.password_validation as validators

from django.contrib.auth.models import User as DjangoUser

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import get_password_validators, validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from accounts.models import User
from bilche_backend import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'password', 'email', 'level', 'fullname', 'phone_number', 'profile_photo', 'is_gardener', 'prefered_hour', '_prefered_days')
        extra_kwargs = {'password': {'write_only': True}, 'email': {'write_only': True}, 'username': {'required': False}}
        # read_only_fields = ()

    def validate_phone_number(self, value):
        pattern = re.compile("^09\d{9}$")
        if pattern.match(value) is None:
            raise serializers.ValidationError("فرمت شماره تلفن همراه نادرست است. "
                                              "شماره تلفن همراه باید با 09 شروع شود و تنها شامل 11 رقم باشد.")
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("کاربری با این شماره تلفن وجود دارد.")
        return value

    def validate_password(self, value):
        try:
            # validate the password against existing validators
            validate_password(
                value,
                user=DjangoUser(username= self.initial_data['email'], email=self.initial_data['email']),
                password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
            )
        except ValidationError as e:
            # raise a validation error for the serializer
            raise e

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


class MyAuthTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = 'نام کاربری یا رمز عبور نادرست است.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'نام کاربری یا رمز عبور نمی تواند خالی باشد.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
