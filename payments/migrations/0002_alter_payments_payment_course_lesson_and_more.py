# Generated by Django 4.2.6 on 2023-10-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_course_lesson',
            field=models.CharField(choices=[('курс', 'курс'), ('урок ', 'урок ')], max_length=50, verbose_name='платеж'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(choices=[('перевод', 'перевод'), ('наличные ', 'наличные ')], default='перевод', max_length=50, verbose_name='способ оплаты'),
        ),
    ]