from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models import Department
from university.serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True, model=Department)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(department, model=Department)
        return Response(serializer.data)

    def create(self, request):
        serializer = DepartmentSerializer(data=request.data, model=Department)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(department, data=request.data, model=Department)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
