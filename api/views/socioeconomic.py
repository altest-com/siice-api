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


class SocioeconomicView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'Socioeconomic'
    queryset = models.Socioeconomic.objects.all()
    serializer_class = serializers.SocioeconomicSerializer

    def get_queryset(self):
        return self.queryset
