from university.models import *

from rest_framework import serializers

class DynamicFieldsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        self.model = kwargs.pop('model', None)
        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            if isinstance(fields, str):
                fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def create(self, validated_data):
        if not self.model:
            raise ValueError("No model specified for serializer.")
        return self.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class SoftDeletedSerializerMixin :
    deleted = serializers.BooleanField(default=False)

class TimestampSerializerMixin :
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

class UserSerializer(DynamicFieldsSerializer, SoftDeletedSerializerMixin, TimestampSerializerMixin):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    address = serializers.CharField(max_length=100)

    class Meta:
        model = User


class DepartmentSerializer(DynamicFieldsSerializer):
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100)
    building = serializers.CharField(max_length=100)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Department


class CourseSerializer(DynamicFieldsSerializer):
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100)
    credits = serializers.IntegerField()
    department = DepartmentSerializer(fields='code', model=Department)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course

class AcademicYearSerializer(DynamicFieldsSerializer):
    start_from = serializers.DateField()
    end_at = serializers.DateField()
    description = serializers.CharField(max_length=255)

    class Meta:
        model = AcademicYear

class SemesterSerializer(DynamicFieldsSerializer):
    name = serializers.CharField(max_length=50)
    academic_year = AcademicYearSerializer(fields='id', model=AcademicYear)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Semester

class TeacherCourseSemesterSerializer(DynamicFieldsSerializer):
    teacher = serializers.SerializerMethodField()
    course = CourseSerializer(fields='id', model=Course)
    semester = SemesterSerializer(fields='id', model=Semester)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TeacherCourseSemester

    def get_teacher(self, obj):
        user = obj.teacher.user
        return UserSerializer(user, fields=('id', 'first_name', 'last_name'), model=User).data


class FeedbackCategorySerializer(DynamicFieldsSerializer):
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100)

    class Meta:
        model = FeedbackCategory



class FeedbackSerializer(DynamicFieldsSerializer):
    user = UserSerializer(fields=('id', 'first_name', 'last_name'), model=User)
    teacher_course_semester = TeacherCourseSemesterSerializer(fields='id', model=TeacherCourseSemester)
    comment = serializers.CharField(max_length=255)
    feedback_category = FeedbackCategorySerializer(fields='name', model=FeedbackCategory)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Feedback



class RoleSerializer(DynamicFieldsSerializer):
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Role


class StudentSerializer(DynamicFieldsSerializer):
    department = DepartmentSerializer(fields='name', model=Department)
    student_year = serializers.IntegerField()
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Student


class TeacherSerializer(DynamicFieldsSerializer):
    department = DepartmentSerializer(fields='name', model=Department)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Teacher