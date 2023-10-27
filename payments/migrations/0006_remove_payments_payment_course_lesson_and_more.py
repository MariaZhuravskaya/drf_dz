# Generated by Django 4.2.6 on 2023-10-20 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0009_delete_payments'),
        ('payments', '0005_alter_payments_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='payment_course_lesson',
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lesson.course', verbose_name='платеж за курс'),
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lesson.lesson', verbose_name='платеж за урок'),
        ),
    ]