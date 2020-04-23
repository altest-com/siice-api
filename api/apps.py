import logging

from django.apps import AppConfig
from django.conf import settings

logger_name = settings.LOGGER_NAME
logger = logging.getLogger(logger_name)


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from . import signals
        try:
            from .services import create_schemas
            create_schemas()
        except Exception as error:
            logger.warning(error)
