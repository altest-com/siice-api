from .evaluation import EvalSection
from django.db import models


class Psychological(EvalSection):

    eval_data = models.OneToOneField(
        'drf_schemas.Item',
        null=True,
        on_delete=models.CASCADE,
        related_name='psychological_eval'
    )
