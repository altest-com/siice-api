from ._abstracts import TrackTimeModel
from django.db import models


class EvalSection(TrackTimeModel):

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_FINISHED = 'finished'

    STATUS_CHOICES = [
        (STATUS_CREATED, 'created'),
        (STATUS_STARTED, 'started'),
        (STATUS_FINISHED, 'finished')
    ]

    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED
    )

    result = models.TextField(blank=True, default='')

    passed = models.BooleanField(blank=True, null=True)

    alert = models.TextField(blank=True, default='')

    started_at = models.DateTimeField(
        null=True,
        blank=True
    )

    finished_at = models.DateTimeField(
        null=True,
        blank=True
    )

    alerted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Evaluation(TrackTimeModel):

    TYPE_ORDINARY = 'ordinary'
    TYPE_EXTRA = 'extra'
    TYPE_REPEAT = 'repeat'

    TYPE_CHOICES = [
        (TYPE_ORDINARY, 'ordinary'),
        (TYPE_EXTRA, 'extra'),
        (TYPE_REPEAT, 'repeat')
    ]

    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        default=TYPE_ORDINARY
    )

    scheduled_at = models.DateTimeField(
        null=True,
        blank=True
    )

    application = models.OneToOneField(
        'Application',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    socioeconomic = models.OneToOneField(
        'Socioeconomic',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    medical = models.OneToOneField(
        'Medical',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    toxicological = models.OneToOneField(
        'Toxicological',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    psychological = models.OneToOneField(
        'Psychological',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    polygraphic = models.OneToOneField(
        'Polygraphic',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )