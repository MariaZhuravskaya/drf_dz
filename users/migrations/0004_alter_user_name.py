# Generated by Django 4.2.6 on 2023-10-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='имя пользователя'),
        ),
    ]
