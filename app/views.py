from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from settings import permissions

from .serializers import (ChangePasswordSerializer,
                          CreateUserProfileSerializer, DefaultMessageFromSerializer,)

# DRF Swagger Schema
from drf_spectacular.utils import (
    extend_schema, OpenApiExample, OpenApiParameter, OpenApiResponse,)


class CreateUser(APIView):
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,)
    serializer_class = CreateUserProfileSerializer

    @extend_schema(
        operation_id="1",
        request=CreateUserProfileSerializer,
        responses={201, OpenApiResponse(
            description="created",
            response=DefaultMessageFromSerializer
        )},
        examples=[
            OpenApiExample(
                name='Create User',
                summary='Payload',
                description='Long description',
                value={"email": "ata@example.com",
                       "password": "strongpassword",
                       "username": "john"
                       },
            )
        ]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChangePassword(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    @extend_schema(
        operation_id="2",
        request=ChangePasswordSerializer,
        responses={200, OpenApiResponse(
            description="created",
            response=ChangePasswordSerializer
        )},
        examples=[
            OpenApiExample(
                name='Change password',
                summary='Payload',
                description='Change your current password to a new one',
                value={
                    "password": "strongpassword",

                },
            )
        ]
    )
    def post(self, request):
        serializer = self.serializer_class(
            context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_201_CREATED)
