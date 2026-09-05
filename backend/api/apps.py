"""API application module."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Task model representation."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
