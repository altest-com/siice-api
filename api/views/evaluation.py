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


class EvaluationView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'Evaluation'
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer

    def get_queryset(self):
        return self.queryset


class AlertView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'Alert'
    queryset = models.Alert.objects.all()
    serializer_class = serializers.AlertSerializer

    def get_queryset(self):
        return self.queryset
