from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    img = models.ImageField(upload_to='lesson/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    video = models.FileField(upload_to='lesson/', verbose_name='ссылка на видео', **NULLABLE)


class Well(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    img = models.ImageField(upload_to='well/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
