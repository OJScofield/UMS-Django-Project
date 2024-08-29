from rest_framework import viewsets, status
from rest_framework.response import Response
from university.serializers import FeedbackSerializer
from university.components import FeedbackComponent

class FeedbackViewSet(viewsets.ViewSet):

    def get_serializer(self, queryset, many=False, fields=None):
        return FeedbackSerializer(queryset, many=many, model=FeedbackSerializer.Meta.model, fields=fields)

    def list(self, request):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None

        feedbacks = FeedbackComponent().get_all_feedbacks()
        serializer = self.get_serializer(feedbacks, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fields = request.query_params.get('fields', None)
        fields = fields.split(',') if fields else None
        feedback_id = int(pk)
        feedback = FeedbackComponent().get_feedback_by_id(feedback_id=feedback_id)
        serializer = self.get_serializer(feedback, fields=fields)
        return Response(serializer.data)

    def create(self, request):
        feedback_data = request.data
        feedback = FeedbackComponent().create_feedback(feedback_data)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        feedback_id = int(pk)
        feedback = FeedbackComponent().update_feedback_by_id(feedback_id, request.data)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        feedback_id = int(pk)
        FeedbackComponent().delete_feedback_by_id(feedback_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
