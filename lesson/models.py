from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    app_label = 'lesson'
    """
    Модель описывающая курс
    """
    name = models.CharField(max_length=150, verbose_name='название курса')
    img = models.ImageField(upload_to='well/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    active = models.BooleanField(default=True, verbose_name='актиный курс')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)


class Lesson(models.Model):
    """
    Модель описывающая урок
    """
    name = models.CharField(max_length=150, verbose_name='название курса')
    img = models.ImageField(upload_to='lesson/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    video = models.URLField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    active = models.BooleanField(default=True, verbose_name='актиный урок')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)


class Subscription(models.Model):
    """
    Модель подписки
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    is_active = models.BooleanField(default=True, verbose_name='активность подписки')

    def __str__(self):
        return f'{self.user}{self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'


