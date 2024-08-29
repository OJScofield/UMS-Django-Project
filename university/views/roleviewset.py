from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models import Role
from university.serializers import RoleSerializer

class RoleViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return RoleSerializer(queryset, many=many, model=Role, fields=fields)

    def list(self, request):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        queryset = Role.objects.all()
        serializer = self.get_serializer(queryset, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(role, fields=fields)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoleSerializer(data=request.data, model=Role)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoleSerializer(role, data=request.data, model=Role)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
