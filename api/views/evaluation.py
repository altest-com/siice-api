from rest_framework import viewsets

from ._mixins import (
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin
)
from .. import models
from .. import serializers


class EvalSectionView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    filter_serializer_class = serializers.EvalSectionFilterSerializer
    multi_query = (
        'status__in'
    )


class EvaluationView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'Evaluation'
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer
    filter_serializer_class = serializers.EvaluationFilterSerializer
    multi_query = (
        'type__in',
        'application__candidate_id__in',
        'application__status__in',
        'application__position__secondment__dependency__corporation_id__in',
        'application__position__secondment__dependency_id__in',
        'application__position__secondment_id__in',
        'application__position_id__in'
    )


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
