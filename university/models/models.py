from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=100, default='John')
    last_name = models.CharField(max_length=100, default='Doe')
    date_of_birth = models.DateField(default=timezone.now)
    email = models.EmailField(unique=True, default='example@example.com')
    phone_number = models.CharField(max_length=15, default='000-000-0000')
    address = models.CharField(max_length=100, default='123 Default St.')
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'user'


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, default='Default Department')
    building = models.CharField(max_length=100, default='Main Building')
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Student {self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = 'student'


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Teacher {self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = 'teacher'


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True, default='Untitled Course')
    code = models.CharField(max_length=20, unique=True, default='COURSE100')
    credits = models.IntegerField(default=3)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course'


class AcademicYear(models.Model):
    start_from = models.DateField(default=timezone.now)
    end_at = models.DateField(default=timezone.now)
    description = models.CharField(max_length=255, default='Academic Year')
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Academic Year {self.start_from} - {self.end_at}"

    class Meta:
        db_table = 'academic_year'


class Semester(models.Model):
    name = models.CharField(max_length=50, unique=True, default='Fall Semester')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, default=1)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'semester'

class TeacherCourseSemester(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=1)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.teacher} - {self.course} - {self.semester}"

    class Meta:
        db_table = 'teacher_course_semester'


class StudentTeacherCourseSemester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    teacher_course_semester = models.ForeignKey(TeacherCourseSemester, on_delete=models.CASCADE, default=1)
    grade = models.CharField(max_length=2, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.teacher_course_semester}"

    class Meta:
        db_table = 'student_teacher_course_semester'