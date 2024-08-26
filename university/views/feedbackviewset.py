from rest_framework import viewsets, status
from rest_framework.response import Response
from university.models import Feedback
from university.serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Feedback.objects.all()
        serializer = FeedbackSerializer(queryset, many=True, model=Feedback)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            feedback = Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FeedbackSerializer(feedback, model=Feedback)
        return Response(serializer.data)

    def create(self, request):
        serializer = FeedbackSerializer(data=request.data, model=Feedback)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            feedback = Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FeedbackSerializer(feedback, data=request.data, model=Feedback)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            feedback = Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
