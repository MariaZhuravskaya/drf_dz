# Generated by Django 4.2.6 on 2023-10-20 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0008_remove_payments_payment_course_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
