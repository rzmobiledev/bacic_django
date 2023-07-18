from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid


class UserManager(BaseUserManager):

    def unique_username(self, email):
        strip = email.replace('@', '_').replace('.com', '').replace('.', '_')
        unique_usr = "%s%s" % (uuid.uuid4().hex[:8], strip)
        return unique_usr

    def create_user(self, email=None, username=None, password=None, **other_fields):
        if not username:
            username = self.unique_username(email)
        if email:
            email = self.normalize_email(email)

        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, username=None, password=None, **other_fields):
        if not username:
            username = self.unique_username(email)
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields["is_staff"] is not True:
            raise ValueError("Superuser must have is_staff=True")
        if other_fields["is_superuser"] is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email, username, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200, null=True,
                            blank=True)
    email = models.EmailField(
        ('Email Address'), unique=True)
    username = models.CharField(
        max_length=200, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()
