"""API application module."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Task model representation."""

    class Meta:
        """Serializer metadata."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
