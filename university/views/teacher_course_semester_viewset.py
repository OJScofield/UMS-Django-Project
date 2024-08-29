from rest_framework import viewsets, status
from rest_framework.response import Response
from university.serializers import TeacherCourseSemesterSerializer
from university.components import TeacherCourseSemesterComponent

class TeacherCourseSemesterViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return TeacherCourseSemesterSerializer(queryset, many=many, model=TeacherCourseSemesterSerializer.Meta.model, fields=fields)

    def list(self, request):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        teacher_course_semesters = TeacherCourseSemesterComponent().get_all_teacher_course_semesters()
        serializer = self.get_serializer(teacher_course_semesters, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None
        teacher_course_semester_id = int(pk)
        teacher_course_semester = TeacherCourseSemesterComponent().get_teacher_course_semester_by_id(teacher_course_semester_id=teacher_course_semester_id)
        serializer = self.get_serializer(teacher_course_semester, fields=fields)
        return Response(serializer.data)

    def create(self, request):
        teacher_course_semester_data = request.data
        teacher_course_semester = TeacherCourseSemesterComponent().create_teacher_course_semester(teacher_course_semester_data)
        serializer = TeacherCourseSemesterSerializer(teacher_course_semester)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        teacher_course_semester_id = int(pk)
        teacher_course_semester = TeacherCourseSemesterComponent().update_teacher_course_semester_by_id(teacher_course_semester_id, request.data)
        serializer = TeacherCourseSemesterSerializer(teacher_course_semester)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        teacher_course_semester_id = int(pk)
        TeacherCourseSemesterComponent().delete_teacher_course_semester_by_id(teacher_course_semester_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
