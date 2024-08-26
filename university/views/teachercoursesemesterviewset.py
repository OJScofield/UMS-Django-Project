from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models import TeacherCourseSemester
from university.serializers import TeacherCourseSemesterSerializer

class TeacherCourseSemesterViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = TeacherCourseSemester.objects.all()
        serializer = TeacherCourseSemesterSerializer(queryset, many=True, model=TeacherCourseSemester)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            teacher_course_semester = TeacherCourseSemester.objects.get(pk=pk)
        except TeacherCourseSemester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherCourseSemesterSerializer(teacher_course_semester, model=TeacherCourseSemester)
        return Response(serializer.data)

    def create(self, request):
        serializer = TeacherCourseSemesterSerializer(data=request.data, model=TeacherCourseSemester)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            teacher_course_semester = TeacherCourseSemester.objects.get(pk=pk)
        except TeacherCourseSemester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherCourseSemesterSerializer(teacher_course_semester, data=request.data, model=TeacherCourseSemester)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            teacher_course_semester = TeacherCourseSemester.objects.get(pk=pk)
        except TeacherCourseSemester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        teacher_course_semester.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
