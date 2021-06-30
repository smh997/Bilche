import re

from rest_framework import serializers

from home_page.models import Bilche_feedback, Bilche_subscribe, Bilche_install_app


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilche_feedback
        fields = ('fullname', 'email', 'text')


class SubscribeSerializer(serializers.Serializer):

    email_phone = serializers.CharField(max_length=50)

    def validate(self, data):
        try:
            if '@' not in data['email_phone']:
                raise Exception('لطفا شماره تلفن همراه یا یک ایمیل معتبر وارد نمایید.'
                                'شماره تلفن همراه باید با 09 شروع شود و تنها شامل 11 رقم باشد.')
        except Exception as e:
            pattern = re.compile("^09\d{9}$")
            if pattern.match(data['email_phone']) is None:
                raise serializers.ValidationError(e)
        return data

    def create(self, validated_data):
        if '@' in validated_data['email_phone']:
            return Bilche_subscribe.objects.create(email=validated_data['email_phone'])
        return Bilche_subscribe.objects.create(phone_number=validated_data['email_phone'])

    def update(self, instance, validated_data):
        pass


class InstallappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilche_install_app
        fields = '__all__'
