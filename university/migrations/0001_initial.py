# Generated by Django 5.1 on 2024-08-22 04:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_from', models.DateField(default=datetime.datetime(2024, 8, 22, 4, 28, 30, 516894, tzinfo=datetime.timezone.utc))),
                ('end_at', models.DateField(default=datetime.datetime(2024, 8, 22, 4, 28, 30, 516894, tzinfo=datetime.timezone.utc))),
                ('description', models.CharField(default='Academic Year', max_length=255)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'academic_year',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Department', max_length=100, unique=True)),
                ('building', models.CharField(default='Main Building', max_length=100)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=100)),
                ('last_name', models.CharField(default='Doe', max_length=100)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2024, 8, 22, 4, 28, 30, 501269, tzinfo=datetime.timezone.utc))),
                ('email', models.EmailField(default='example@example.com', max_length=254, unique=True)),
                ('phone_number', models.CharField(default='000-000-0000', max_length=15)),
                ('address', models.CharField(default='123 Default St.', max_length=100)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Course', max_length=100, unique=True)),
                ('code', models.CharField(default='COURSE100', max_length=20, unique=True)),
                ('credits', models.IntegerField(default=3)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.department')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Fall Semester', max_length=50, unique=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('academic_year', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.academicyear')),
            ],
            options={
                'db_table': 'semester',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.department')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.user')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.department')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.user')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='StudentTeacherCourseSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, max_length=2, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.course')),
                ('semester', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.semester')),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.student')),
                ('teacher', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.teacher')),
            ],
            options={
                'db_table': 'student_teacher_course_semester',
            },
        ),
    ]
