from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from core.exception import AuthException


class EmailAuthBackend(ModelBackend):
    """
    Custom authentication backend.

    Allows users to log in using their email address.
    """

    def authenticate(self, request, username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = get_user_model().objects.get(
                Q(username__iexact=username) | Q(email__iexact=username))
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            raise AuthException()

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
