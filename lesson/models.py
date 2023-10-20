from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    img = models.ImageField(upload_to='well/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    active = models.BooleanField(default=True, verbose_name='актиный курс')


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    img = models.ImageField(upload_to='lesson/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    video = models.URLField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    active = models.BooleanField(default=True, verbose_name='актиный урок')


