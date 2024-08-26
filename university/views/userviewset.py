from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models import User, Student, Teacher
from university.serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        user_type = request.query_params.get('user_type', None)
        if user_type == 'STUDENT':
            queryset = Student.objects.all()
            serializer = UserSerializer(queryset, many=True, model=User)
        elif user_type == 'TEACHER':
            queryset = Teacher.objects.all()
            serializer = UserSerializer(queryset, many=True, model=User)
        else:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True, model=User)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, model=User)
        return Response(serializer.data)

    def create(self, request):
        user_type = request.data.get('user_type', None)
        if user_type == 'STUDENT':
            serializer = StudentSerializer(data=request.data, model=Student)
        elif user_type == 'TEACHER':
            serializer = TeacherSerializer(data=request.data, model=Teacher)
        else:
            serializer = UserSerializer(data=request.data, model=User)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, model=User)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
