# Generated by Django 4.2.6 on 2023-10-18 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_rename_well_course_alter_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lesson.course'),
            preserve_default=False,
        ),
    ]
