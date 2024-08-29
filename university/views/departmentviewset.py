from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models import Department
from university.serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return DepartmentSerializer(queryset, many=many, model=Department, fields=fields)

    def list(self, request):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        queryset = Department.objects.all()
        serializer = self.get_serializer(queryset, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(department, fields=fields)
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
