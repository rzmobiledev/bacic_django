from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class AuthException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = {"detail": "User not found"}
    default_code = "User has no credential access"


class ParseError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Malformed request.')
    default_code = 'parse_error'


class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Incorrect authentication credentials.')
    default_code = 'authentication_failed'


class NotAuthenticated(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Authentication credentials were not provided.')
    default_code = 'not_authenticated'


class PermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('You do not have permission to perform this action.')
    default_code = 'permission_denied'
