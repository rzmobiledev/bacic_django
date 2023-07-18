from django.urls import path
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app.views import CreateUser, ChangePassword


app_name = 'app'

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create-user/', CreateUser.as_view(), name='create-user'),
    path('changepass/', ChangePassword.as_view(), name='changepass'),
]
