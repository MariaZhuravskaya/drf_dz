# Generated by Django 4.2.6 on 2023-10-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, max_length=20, verbose_name='имя пользователя'),
            preserve_default=False,
        ),
    ]
