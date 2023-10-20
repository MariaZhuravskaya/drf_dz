from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    name = models.CharField(max_length=20, verbose_name='имя пользователя')
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
