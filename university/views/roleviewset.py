from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models import Role
from university.serializers import RoleSerializer

class RoleViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True, model=Role)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoleSerializer(role, model=Role)
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
