# Generated by Django 5.1 on 2024-08-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_alter_course_code_alter_feedbackcategory_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_year',
            field=models.IntegerField(default=1),
        ),
    ]
