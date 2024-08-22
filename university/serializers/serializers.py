from rest_framework import serializers
from university.models.models import Student, Course, Teacher, Semester, StudentTeacherCourseSemester

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


class StudentTeacherCourseSemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTeacherCourseSemester
        fields = '__all__'

