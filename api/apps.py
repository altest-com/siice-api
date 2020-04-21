from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from . import signals
        from .services import create_schemas
        create_schemas()
