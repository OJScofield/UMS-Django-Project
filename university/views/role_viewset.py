from rest_framework import viewsets, status
from rest_framework.response import Response
from university.serializers import RoleSerializer
from university.components import RoleComponent

class RoleViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return RoleSerializer(queryset, many=many, model=RoleSerializer.Meta.model, fields=fields)

    def list(self, request):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        roles = RoleComponent().get_all_roles()
        serializer = self.get_serializer(roles, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None
        role_id = int(pk)
        role = RoleComponent().get_role_by_id(role_id=role_id)
        serializer = self.get_serializer(role, fields=fields)
        return Response(serializer.data)

    def create(self, request):
        role_data = request.data
        role = RoleComponent().create_role(role_data)
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        role_id = int(pk)
        role = RoleComponent().update_role_by_id(role_id, request.data)
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        role_id = int(pk)
        RoleComponent().delete_role_by_id(role_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
