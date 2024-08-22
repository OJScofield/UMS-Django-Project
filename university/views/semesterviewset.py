from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models.models import Semester
from university.serializers.serializers import SemesterSerializer

class SemesterViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Semester.objects.all()
        serializer = SemesterSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            semester = Semester.objects.get(pk=pk)
        except Semester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SemesterSerializer(semester)
        return Response(serializer.data)

    def create(self, request):
        serializer = SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            semester = Semester.objects.get(pk=pk)
        except Semester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SemesterSerializer(semester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            semester = Semester.objects.get(pk=pk)
        except Semester.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        semester.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)