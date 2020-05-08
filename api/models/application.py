from django.utils.functional import cached_property

from ._abstracts import TrackTimeModel
from django.db import models


class Candidate(TrackTimeModel):

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    curp = models.CharField(max_length=255)

    image = models.OneToOneField(
        'Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='candidate'
    )


class Corporation(TrackTimeModel):

    name = models.CharField(max_length=255)


class Dependency(TrackTimeModel):

    name = models.CharField(max_length=255)

    corporation = models.ForeignKey(
        'Corporation',
        on_delete=models.CASCADE,
        related_name='dependencies'
    )


class Secondment(TrackTimeModel):

    name = models.CharField(max_length=255)

    dependency = models.ForeignKey(
        'Dependency',
        on_delete=models.CASCADE,
        related_name='secondments'
    )

    @cached_property
    def corporation(self):
        # noinspection PyUnresolvedReferences
        return self.dependency.corporation


class Position(TrackTimeModel):

    name = models.CharField(max_length=255)

    secondment = models.ForeignKey(
        'Secondment',
        on_delete=models.CASCADE,
        related_name='positions'
    )

    @cached_property
    def dependency(self):
        # noinspection PyUnresolvedReferences
        return self.secondment.dependency

    @cached_property
    def corporation(self):
        # noinspection PyUnresolvedReferences
        return self.dependency.corporation


class Application(TrackTimeModel):

    STATUS_CREATED = 'created'
    STATUS_ACCEPTED = 'accepted'
    STATUS_REJECTED = 'rejected'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = [
        (STATUS_CREATED, 'created'),
        (STATUS_ACCEPTED, 'accepted'),
        (STATUS_REJECTED, 'rejected'),
        (STATUS_ARCHIVED, 'archived')
    ]

    document = models.CharField(max_length=255)

    year = models.IntegerField()

    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED
    )

    candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
        related_name='applications'
    )

    position = models.ForeignKey(
        'Position',
        on_delete=models.SET_NULL,
        null=True,
        related_name='applications'
    )

    accepted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    rejected_at = models.DateTimeField(
        null=True,
        blank=True
    )

    archived_at = models.DateTimeField(
        null=True,
        blank=True
    )

    @cached_property
    def secondment(self):
        # noinspection PyUnresolvedReferences
        return self.position.secondment

    @cached_property
    def dependency(self):
        # noinspection PyUnresolvedReferences
        return self.secondment.dependency

    @cached_property
    def corporation(self):
        # noinspection PyUnresolvedReferences
        return self.dependency.corporation
