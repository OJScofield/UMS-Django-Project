from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from university.constants import *
from university.serializers import UserSerializer, StudentSerializer, TeacherSerializer
from university.components import UserComponent, RoleComponent, CourseComponent


class UserViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return UserSerializer(queryset, many=many, model=UserSerializer.Meta.model, fields=fields)

    def list(self, request):
        user_type = request.query_params.get('user_type', None)
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        users = UserComponent().get_all_users(user_type=user_type)
        serializer = self.get_serializer(users, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None
        user_id = int(pk)
        user = UserComponent().get_user_by_id(user_id=user_id)
        serializer = self.get_serializer(user, fields=fields)
        return Response(serializer.data)

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
