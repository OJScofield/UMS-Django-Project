from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models.models import Student, StudentTeacherCourseSemester
from university.serializers.serializers import StudentSerializer

class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student)
        response = Response(serializer.data)

        courses = StudentTeacherCourseSemester.objects.filter(student=student).select_related(
            'teacher_course_semester__course')

        course_data = [
            {
                'id': course.teacher_course_semester.course.id,
                'name': course.teacher_course_semester.course.name,
                'code': course.teacher_course_semester.course.code,
            }
            for course in courses
        ]

        response.data['courses'] = course_data
        return response

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
