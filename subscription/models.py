from django.db import models

from lesson.models import Course


class Subscription(models.Model):
    """
    Модель подписки
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    user = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='пользователь')
    is_active = models.BooleanField(default=True, verbose_name='активность подписки')
