from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class SignUpConfig(AppConfig):
    name = 'sign_up'


class User(AbstractUser):
    user_type = models.CharField(max_length=5)