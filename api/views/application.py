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


class CandidateView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Candidate'
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer
    filter_serializer_class = serializers.CandidateFilterSerializer


class CorporationView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Corporation'
    queryset = models.Corporation.objects.all()
    serializer_class = serializers.CorporationSerializer
    filter_serializer_class = serializers.CorporationFilterSerializer


class DependencyView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Dependency'
    queryset = models.Dependency.objects.all()
    serializer_class = serializers.DependencySerializer
    filter_serializer_class = serializers.DependencyFilterSerializer
    multi_query = ('corporation_id__in',)


class SecondmentView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Secondment'
    queryset = models.Secondment.objects.all()
    serializer_class = serializers.SecondmentSerializer
    filter_serializer_class = serializers.SecondmentFilterSerializer
    multi_query = ('dependency_id__in', 'dependency__corporation_id__in')


class PositionView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Position'
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer
    filter_serializer_class = serializers.PositionFilterSerializer
    multi_query = (
        'secondment_id__in',
        'secondment__dependency_id__in',
        'secondment__dependency__corporation_id__in'
    )


class ApplicationView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    FilterMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Application'
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer
    filter_serializer_class = serializers.ApplicationFilterSerializer
    multi_query = (
        'status__in',
        'candidate_id__in',
        'position__secondment__dependency__corporation_id__in',
        'position__secondment__dependency_id__in',
        'position__secondment_id__in',
        'position_id__in'
    )