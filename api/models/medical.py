from .evaluation import EvalSection
from django.db import models


class Medical(EvalSection):

    eval_data = models.OneToOneField(
        'drf_schemas.Item',
        null=True,
        on_delete=models.CASCADE,
        related_name='medical_eval'
    )
