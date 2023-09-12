from django.contrib.auth.models import AbstractUser
from django.db import models

from constants import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='phone', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='city', **NULLABLE)
    avatar = models.ImageField(upload_to='user/', verbose_name='avatar', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

