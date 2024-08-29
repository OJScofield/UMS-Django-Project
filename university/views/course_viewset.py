from rest_framework import viewsets, status
from rest_framework.response import Response
from university.serializers import CourseSerializer
from university.components import CourseComponent

class CourseViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return CourseSerializer(queryset, many=many, model=CourseSerializer.Meta.model, fields=fields)

    def list(self, request):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        courses = CourseComponent().get_all_courses()
        serializer = self.get_serializer(courses, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None
        course_id = int(pk)
        course = CourseComponent().get_course_by_id(course_id=course_id)
        serializer = self.get_serializer(course, fields=fields)
        return Response(serializer.data)

    def create(self, request):
        course_data = request.data
        course = CourseComponent().create_course(course_data)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        course_id = int(pk)
        course = CourseComponent().update_course_by_id(course_id, request.data)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        course_id = int(pk)
        CourseComponent().delete_course_by_id(course_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
