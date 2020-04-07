from rest_framework import viewsets

from ._mixins import (
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
)
from .. import models
from .. import serializers


class PsychologicalView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'Psychological'
    queryset = models.Psychological.objects.all()
    serializer_class = serializers.PsychologicalSerializer

    def get_queryset(self):
        return self.queryset

