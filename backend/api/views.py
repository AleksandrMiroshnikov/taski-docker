"""API application module."""

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """Task model representation."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """Process the request and return data."""
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
