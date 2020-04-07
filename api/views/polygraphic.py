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


class PolygraphicView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'Polygraphic'
    queryset = models.Polygraphic.objects.all()
    serializer_class = serializers.PolygraphicSerializer

    def get_queryset(self):
        return self.queryset
