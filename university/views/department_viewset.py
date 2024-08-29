from rest_framework import viewsets, status
from rest_framework.response import Response
from university.serializers import DepartmentSerializer
from university.components import DepartmentComponent

class DepartmentViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return DepartmentSerializer(queryset, many=many, model=DepartmentSerializer.Meta.model, fields=fields)

    def list(self, request):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        departments = DepartmentComponent().get_all_departments()
        serializer = self.get_serializer(departments, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None
        department_id = int(pk)
        department = DepartmentComponent().get_department_by_id(department_id=department_id)
        serializer = self.get_serializer(department, fields=fields)
        return Response(serializer.data)

    def create(self, request):
        department_data = request.data
        department = DepartmentComponent().create_department(department_data)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        department_id = int(pk)
        department = DepartmentComponent().update_department_by_id(department_id, request.data)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        department_id = int(pk)
        DepartmentComponent().delete_department_by_id(department_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
