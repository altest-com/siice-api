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


class ToxicologicalView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'Toxicological'
    queryset = models.Toxicological.objects.all()
    serializer_class = serializers.ToxicologicalSerializer

    def get_queryset(self):
        return self.queryset
