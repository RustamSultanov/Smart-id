from rest_framework import serializers
from . import models
from django.utils.translation import gettext_lazy as _


class RegisterAccountSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    def validate(self, data):
        try:
            models.SmartId.objects.get(phone_number=data.get('phone_number'))
            models.SmartId.objects.get(email=data.get('email'))
            raise serializers.ValidationError(_("Электронный адресс или номер телефона уже заняты"))
        except models.SmartId.DoesNotExist:
            pass

        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError(_("Вы забыли ввести пароль"))

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(_("Пароли не совпадают"))

        return data

    class Meta:
        model = models.Employee
        fields = (
        'email', 'phone_number', 'first_name', 'last_name', 'patronymic', 'password', 'confirm_password', 'sex')
        extra_kwargs = {'confirm_password': {'read_only': True}}


class RegisterSmartIdSerializer(RegisterAccountSerializer):
    class Meta:
        model = models.SmartId
        fields = (
        'email', 'phone_number', 'first_name', 'last_name', 'patronymic', 'password', 'confirm_password', 'sex',
        'resident', 'inn', 'photo', 'contacts', 'passport_scan', 'specialization', 'description', 'status')
        extra_kwargs = {'confirm_password': {'read_only': True}}


class RegisterBusinessSmartIdSerializer(RegisterAccountSerializer):
    class Meta:
        model = models.SmartId
        fields = (
        'email', 'phone_number', 'first_name', 'last_name', 'patronymic', 'password', 'confirm_password', 'sex',
        'resident', 'inn', 'photo', 'contacts', 'passport_scan', 'specialization')
        extra_kwargs = {'confirm_password': {'read_only': True}}
