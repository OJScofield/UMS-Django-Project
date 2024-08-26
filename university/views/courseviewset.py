from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models import Course
from university.serializers import CourseSerializer

class CourseViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True, model=Course)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course, model=Course)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourseSerializer(data=request.data, model=Course)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course, data=request.data, model=Course)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
