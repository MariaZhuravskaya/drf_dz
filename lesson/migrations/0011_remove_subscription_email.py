# Generated by Django 4.2.6 on 2023-10-27 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0010_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='email',
        ),
    ]
