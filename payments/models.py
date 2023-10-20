from django.db import models

from users.models import User


class Payments(models.Model):

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
    payment_course_lesson = models.CharField(max_length=50, choices=PAYMENTS_COURSE_LESSON, verbose_name='платеж')



