# Generated by Django 5.1 on 2024-08-22 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_studentteachercoursesemester_ali'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentteachercoursesemester',
            name='ali',
        ),
    ]
