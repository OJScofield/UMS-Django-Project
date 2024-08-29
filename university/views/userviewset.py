from rest_framework import viewsets, status
from rest_framework.response import Response
from university.serializers import UserSerializer
from university.components import UserComponent
from university.exceptions import ResourceException

class UserViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return UserSerializer(queryset, many=many, model=UserSerializer.Meta.model, fields=fields)

    def list(self, request):
        user_type = request.query_params.get('user_type', None)
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        users = UserComponent().get_all_users(user_type=user_type)
        serializer = self.get_serializer(users, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None
        user_id = int(pk)
        if user_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = UserComponent().get_user_by_id(user_id=user_id)
        serializer = self.get_serializer(user, fields=fields)
        return Response(serializer.data)

    def create(self, request):
        user_type = request.data.get('user_type', None)
        serializer_class = UserComponent().get_serializer_class(user_type)
        serializer = serializer_class(data=request.data, model=serializer_class.Meta.model)

        if serializer.is_valid():
            UserComponent().create_user(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user_id = int(pk)
        user_serializer = UserSerializer(user_id, data=request.data, model=UserSerializer.Meta.model)
        x = user_serializer.is_valid()
        if True:
            first_name = user_serializer.data.get('first_name', None)
            last_name = user_serializer.data.get('last_name', None)
            UserComponent().update_user_by_id(user_id, first_name=first_name, last_name=last_name)

            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            user_id = int(pk)
            UserComponent().delete_user_by_id(user_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ResourceException:
            return Response(status=status.HTTP_404_NOT_FOUND)