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


class CandidateView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Candidate'
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer

    def get_queryset(self):
        return self.queryset


class CorporationView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Corporation'
    queryset = models.Corporation.objects.all()
    serializer_class = serializers.CorporationSerializer

    def get_queryset(self):
        return self.queryset


class DependencyView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Dependency'
    queryset = models.Dependency.objects.all()
    serializer_class = serializers.DependencySerializer

    def get_queryset(self):
        return self.queryset


class SecondmentView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Secondment'
    queryset = models.Secondment.objects.all()
    serializer_class = serializers.SecondmentSerializer

    def get_queryset(self):
        return self.queryset


class PositionView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Position'
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer

    def get_queryset(self):
        return self.queryset


class ApplicationView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Application'
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

    def get_queryset(self):
        return self.queryset