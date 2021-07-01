import re

from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import get_password_validators, validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.fields import empty

from accounts.models import User
from bilche_backend import settings

#
# ERROR_MESSAGES = {
#     "blank": "این فیلد الزامی است",
#     "null": "این فیلد الزامی است",
#     "required": "این فیلد الزامی است",
#     "invalid": "قالب این فیلد صحیح نمی‌باشد",
#     "max_length": "اندازه‌ی این ورودی طولانی است",
#     "min_length": "اندازه‌ی این ورودی کوچک است.",
#     "unique": "این فیلد تکراری است",
#     "unique_together": "این فیلدها تکرارین"
# }
#
#
# class ModelSerializer(serializers.ModelSerializer):
#     """
#     overwrite serializer.ModelSerializer for customize some thing it
#     """
#
#     def __init__(self, instance=None, data=empty, **kwargs):
#         super(ModelSerializer, self).__init__(instance, data, **kwargs)
#         for field in self.fields:
#             self.fields[field].error_messages.update(ERROR_MESSAGES)
#
#
# class Serializer(serializers.Serializer):
#     """
#     overwrite Serializer with persian error
#     """
#
#     def __init__(self, instance=None, data=empty, **kwargs):
#         super(Serializer, self).__init__(instance, data, **kwargs)
#         for field in self.fields:
#             self.fields[field].error_messages.update(ERROR_MESSAGES)
#
#     def update(self, instance, validated_data):
#         pass
#
#     def create(self, validated_data):
#         pass

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
                msg = {'error': 'نام کاربری یا رمز عبور نادرست است.'}
                raise serializers.ValidationError(msg)
        else:
            msg = {'error': 'نام کاربری یا رمز عبور نمی تواند خالی باشد.'}
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'password', 'email', 'level', 'fullname', 'phone_number', 'profile_photo', 'is_gardener', 'prefered_hour', '_prefered_days')
        extra_kwargs = {'password': {'write_only': True}, 'email': {'write_only': True}, 'username': {'required': False}}
        # read_only_fields = ()

    def validate_phone_number(self, value):
        pattern = re.compile("^09\d{9}$")
        if pattern.match(value) is None:
            raise serializers.ValidationError('فرمت شماره تلفت همراه نادرست است.'
                                                               'شماره تلفن همراه باید با 09 شروع شود و تنها شامل 11 رقم باشد.')
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("کاربری با این شماره تلفن وجود دارد.")
        return value

    def validate_password(self, value):
        try:
            # validate the password against existing validators
            validate_password(
                value,
                user=DjangoUser(username=self.initial_data['email'], email=self.initial_data['email']),
                password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
            )
        except ValidationError as e:
            raise serializers.ValidationError('این رمز به اندازه کافی امن نیست.'
                                                           'رمز نمی تواند کوتاه تر از 8 کاراکتر یا فقط شامل اعداد باشد.')
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

