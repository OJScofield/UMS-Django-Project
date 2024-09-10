from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from university.constants import USER_TYPE_STUDENT, USER_TYPE_TEACHER
from university.serializers import UserSerializer, StudentSerializer, TeacherSerializer, CourseSerializer
from university.components import UserComponent, CourseComponent, RoleComponent

class UserViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        if fields is not None:
            return UserSerializer(queryset, many=many, model=UserSerializer.Meta.model, fields=fields)
        return UserSerializer(queryset, many=many, model=UserSerializer.Meta.model)

    def list(self, request):
        user_type = request.query_params.get('user_type', None)

        fields = ['id', 'first_name', 'last_name', 'email']

        if user_type == USER_TYPE_STUDENT:
            users = UserComponent().get_all_users(user_type=USER_TYPE_STUDENT)
        elif user_type == USER_TYPE_TEACHER:
            users = UserComponent().get_all_users(user_type=USER_TYPE_TEACHER)
        else:
            users = UserComponent().get_all_users()

        if not users:
            return Response({'detail': 'No users found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(users, many=True, fields=fields)
        user_data = serializer.data

        if user_type == USER_TYPE_STUDENT:
            for user in user_data:
                courses = CourseComponent().get_courses_by_student_id(user['id'])
                course_serializer = CourseSerializer(courses, many=True)
                user['courses'] = course_serializer.data

        return Response(user_data)

    def retrieve(self, request, pk=None):
        user_id = int(pk)
        fields = ['id', 'first_name', 'last_name', 'email']

        user = UserComponent().get_user_by_id(user_id=user_id)
        serializer = self.get_serializer(user, fields=fields)
        user_data = serializer.data

        # Check if the user is a student and include their courses
        if UserComponent().is_student(user_id):
            courses = CourseComponent().get_courses_by_student_id(user_id)
            course_serializer = CourseSerializer(courses, many=True)
            user_data['courses'] = course_serializer.data

        return Response(user_data)

    def create(self, request):
        user_type = request.data.get('user_type', None)

        if user_type == USER_TYPE_STUDENT:
            serializer_class = StudentSerializer
        elif user_type == USER_TYPE_TEACHER:
            serializer_class = TeacherSerializer
        else:
            serializer_class = UserSerializer

        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            UserComponent().create_user(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        user_id = int(pk)
        user_serializer = UserSerializer(user_id, data=request.data, model=UserSerializer.Meta.model)
        user_serializer.is_valid()
        first_name = user_serializer.data.get('first_name', None)
        last_name = user_serializer.data.get('last_name', None)
        UserComponent().update_user_by_id(user_id, first_name=first_name, last_name=last_name)

        return Response(user_serializer.data)

    def destroy(self, request, pk=None):
        user_id = int(pk)
        UserComponent().delete_user_by_id(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'], url_path='overview')
    def overview(self, request):
        total_users = UserComponent().get_total_users()
        total_students = UserComponent().get_total_students()
        total_teachers = UserComponent().get_total_teachers()
        total_roles = RoleComponent().get_total_roles()
        total_courses = CourseComponent().get_total_courses()

        overview_data = {
            'total_users': total_users,
            'total_students': total_students,
            'total_teachers': total_teachers,
            'total_roles': total_roles,
            'total_courses': total_courses,
        }
        return Response(overview_data, status=status.HTTP_200_OK)
