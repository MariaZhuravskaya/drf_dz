from django.db import models

from lesson.models import Course, Lesson
from users.models import User


class Payments(models.Model):
    """
     Модель описывающая платеж
     """
    PAYMENTS_METHOT = [
        ("перевод", "перевод"),
        ("наличные", "наличные"),
    ]

    PAYMENTS_COURSE_LESSON = [
        ("курс", "курс"),
        ("урок", "урок"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, default='перевод', choices=PAYMENTS_METHOT, verbose_name="способ оплаты")
    payment_course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='платеж за курс', null=True, blank=True)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT, verbose_name='платеж за урок', null=True, blank=True)
    card = models.CharField(max_length=16, default='4242424242424242', verbose_name="карта")



