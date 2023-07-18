from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _

# log
from logger.log import Log

from .models import User


class UserResponseCreatedSerializer(APIException):
    status_code = 201
    default_detail = _('User created')
    default_code = 'Created'


class DefaultMessageFromSerializer(serializers.Serializer):
    detail = serializers.CharField()


class CreateUserProfileSerializer(serializers.Serializer):

    name = serializers.CharField(
        max_length=200, required=False, allow_null=True)
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=250, write_only=True)

    def create(self, data):
        try:
            password = data.pop('password')
            user = User.objects.create(**data)
            user.set_password(password)
            user.is_active = True
            user.save()
            return user
        except Exception as e:
            Log.error(str(e))
            return None


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input-type": "password"}, required=True)
    new_password = serializers.CharField(
        style={"input-type": "password"}, required=True)

    def validate_current_password(self, val):
        if not self.context['request'].user.check_password(val):
            raise serializers.ValidationError(
                {"current_password": "Does not match"})
        return val
