import re

from django.contrib.auth.hashers import make_password
from django.db.models import Max
from rest_framework import serializers

from accounts.models import User


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

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
