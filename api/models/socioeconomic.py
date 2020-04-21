from .evaluation import EvalSection
from django.db import models


class Socioeconomic(EvalSection):

    eval_data = models.OneToOneField(
        'drf_schemas.Item',
        null=True,
        on_delete=models.CASCADE,
        related_name='socioeconomic_eval'
    )

    DIGI_ENTRY_EMPTY = 'empty'

    DIGI_ENTRY_CHOICES = [
        (DIGI_ENTRY_EMPTY, 'empty')
    ]

    ID_TYPE_INE = 'ine'
    ID_TYPE_PASSPORT = 'passport'

    ID_TYPE_CHOICES = [
        (ID_TYPE_INE, 'ine'),
        (ID_TYPE_PASSPORT, 'passport'),
    ]

    digi_entry = models.CharField(
        max_length=64,
        choices=DIGI_ENTRY_CHOICES,
        blank=True,
        default=''
    )

    digi_date = models.DateField(
        null=True,
        blank=True
    )

    digi_id_type = models.CharField(
        max_length=64,
        choices=ID_TYPE_CHOICES,
        blank=True,
        default=''
    )

    digi_id_number = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )

    digi_image = models.OneToOneField(
        'Image',
        on_delete=models.SET_NULL,
        related_name='socioeconomic_digi',
        null=True,
        blank=True
    )
