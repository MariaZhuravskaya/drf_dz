from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member'
    MODERATOR = 'moderator'


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    name = models.CharField(max_length=20, verbose_name='имя пользователя', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='роль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



