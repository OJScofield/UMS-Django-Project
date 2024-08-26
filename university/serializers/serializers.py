from rest_framework import serializers
from university.models import Course, Department, Feedback, Role, TeacherCourseSemester, User, Student, Teacher


class DynamicFieldsSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        self.model = kwargs.pop('model', None)
        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
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


class UserSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    address = serializers.CharField(max_length=100)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = User


class DepartmentSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100)
    building = serializers.CharField(max_length=100)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Department


class CourseSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100)
    credits = serializers.IntegerField()
    department = DepartmentSerializer(fields=('id', 'name', 'code'), model=Department)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Course


class TeacherCourseSemesterSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    teacher = UserSerializer(fields=('id', 'first_name', 'last_name'), model=User)
    course = CourseSerializer(fields=('id', 'name', 'code'), model=Course)
    semester = serializers.IntegerField()
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = TeacherCourseSemester


class FeedbackSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(fields=('id', 'first_name', 'last_name'), model=User)
    teacher_course_semester = TeacherCourseSemesterSerializer(fields=('id',), model=TeacherCourseSemester)
    comment = serializers.CharField(max_length=255)
    feedback_category = serializers.IntegerField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Feedback


class RoleSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Role


class StudentSerializer(UserSerializer):
    department = DepartmentSerializer(fields=('id', 'name', 'code'), model=Department)
    student_year = serializers.IntegerField()
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Student


class TeacherSerializer(UserSerializer):
    department = DepartmentSerializer(fields=('id', 'name', 'code'), model=Department)
    deleted = serializers.BooleanField(default=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Teacher
