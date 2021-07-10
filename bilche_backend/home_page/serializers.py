import re

from django.core.exceptions import ValidationError
from rest_framework import serializers

from home_page.models import BilcheFeedback, BilcheSubscribe, BilcheInstallapp


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilcheFeedback
        fields = ('fullname', 'email', 'text')


class SubscribeSerializer(serializers.Serializer):

    email_phone = serializers.CharField(max_length=50)

    def validate(self, data):
        try:
            if '@' not in data['email_phone']:
                raise ValidationError('لطفا شماره تلفن همراه یا یک ایمیل معتبر وارد نمایید.'
                                'شماره تلفن همراه باید با 09 شروع شود و تنها شامل 11 رقم باشد.')
            elif BilcheSubscribe.objects.filter(email=data['email_phone']).exists():
                raise ValidationError('کاربری با این ایمیل قبلا در خبرنامه بیلچه ثبت نام شده است.')
        except ValidationError as e:
            pattern = re.compile("^09\d{9}$")
            if pattern.match(data['email_phone']) is None:
                raise serializers.ValidationError(e)
            elif BilcheSubscribe.objects.filter(phone_number=data['email_phone']).exists():
                raise ValidationError('کاربری با این شماره تلفن قبلا در خبرنامه بیلچه ثبت نام شده است.')
        return data

    def create(self, validated_data):
        if '@' in validated_data['email_phone']:
            return BilcheSubscribe.objects.create(email=validated_data['email_phone'])
        return BilcheSubscribe.objects.create(phone_number=validated_data['email_phone'])

    def update(self, instance, validated_data):
        pass


class InstallappSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilcheInstallapp
        fields = '__all__'
