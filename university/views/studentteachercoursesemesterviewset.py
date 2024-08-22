from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models.models import StudentTeacherCourseSemester
from university.serializers.serializers import StudentTeacherCourseSemesterSerializer

class StudentTeacherCourseSemesterViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = StudentTeacherCourseSemester.objects.all()
        serializer = StudentTeacherCourseSemesterSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            student_teacher_course_semester = StudentTeacherCourseSemester.objects.get(pk=pk)
        except StudentTeacherCourseSemester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentTeacherCourseSemesterSerializer(student_teacher_course_semester)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentTeacherCourseSemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            student_teacher_course_semester = StudentTeacherCourseSemester.objects.get(pk=pk)
        except StudentTeacherCourseSemester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentTeacherCourseSemesterSerializer(student_teacher_course_semester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            student_teacher_course_semester = StudentTeacherCourseSemester.objects.get(pk=pk)
        except StudentTeacherCourseSemester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student_teacher_course_semester.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
