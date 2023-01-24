from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
