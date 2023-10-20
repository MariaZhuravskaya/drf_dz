# Generated by Django 4.2.6 on 2023-10-20 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lesson', '0005_lesson_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True, verbose_name='актиный курс'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='active',
            field=models.BooleanField(default=True, verbose_name='актиный урок'),
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата оплаты')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('перевод', 'перевод'), ('наличные ', 'наличные ')], default='перевод ', max_length=50, verbose_name='способ оплаты')),
                ('payment_course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.course', verbose_name='платеж за курс')),
                ('payment_lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.lesson', verbose_name='платеж за урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
