# Generated by Django 4.2.6 on 2023-10-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название курса')),
                ('img', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='картинка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('video', models.FileField(upload_to='lesson/', verbose_name='ссылка на видео')),
            ],
        ),
    ]
