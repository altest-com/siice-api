from rest_framework import serializers
from ._abstracts import (
    TrackTimeSerializer,
    MaskFieldSerializer,
    descent_orders
)
from .. import models


class CandidateSerializer(MaskFieldSerializer, TrackTimeSerializer):

    # Required
    name = serializers.CharField(
        required=True,
        help_text='Candidate name'
    )
    last_name = serializers.CharField(
        required=True,
        help_text='Candidate last name'
    )
    curp = serializers.CharField(
        required=True,
        help_text='Candidate CURP'
    )
    image = serializers.PrimaryKeyRelatedField(
        queryset=models.Image.objects.all(),
        required=False,
        help_text='Candidate image'
    )

    class Meta:
        model = models.Candidate
        fields = TrackTimeSerializer.Meta.fields + (
            'name',
            'last_name',
            'curp',
            'image'
        )


class CandidateFilterSerializer(serializers.Serializer):

    name__icontains = serializers.CharField(required=False)
    last_name__icontains = serializers.CharField(required=False)
    curp__icontains = serializers.CharField(required=False)
    created_at__gte = serializers.DateTimeField(required=False)
    created_at__lte = serializers.DateTimeField(required=False)

    order_by = serializers.ChoiceField(
        choices=descent_orders((
            'name',
            'last_name',
            'curp',
            'created_at'
        )),
        required=False
    )


class CorporationSerializer(TrackTimeSerializer, MaskFieldSerializer):

    # Required
    name = serializers.CharField(
        required=True,
        help_text='Corporation name'
    )

    class Meta:
        model = models.Corporation
        fields = TrackTimeSerializer.Meta.fields + (
            'name',
        )


class CorporationFilterSerializer(serializers.Serializer):

    name__icontains = serializers.CharField(required=False)
    created_at__gte = serializers.DateTimeField(required=False)
    created_at__lte = serializers.DateTimeField(required=False)

    order_by = serializers.ChoiceField(
        choices=descent_orders((
            'name',
            'created_at',
            '-name',
            '-created_at',
        )),
        required=False
    )


class DependencySerializer(TrackTimeSerializer, MaskFieldSerializer):

    # Required
    name = serializers.CharField(
        required=True,
        help_text='Corporation name'
    )
    corporation = serializers.PrimaryKeyRelatedField(
        queryset=models.Corporation.objects.all(),
        required=True,
        help_text='Dependency corporation'
    )

    class Meta:
        model = models.Dependency
        fields = TrackTimeSerializer.Meta.fields + (
            'name',
            'corporation'
        )


class DependencyFilterSerializer(serializers.Serializer):

    name__icontains = serializers.CharField(required=False)
    corporation_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )
    created_at__gte = serializers.DateTimeField(required=False)
    created_at__lte = serializers.DateTimeField(required=False)

    order_by = serializers.ChoiceField(
        choices=descent_orders((
            'name',
            'created_at',
            'corporation__name'
        )),
        required=False
    )


class SecondmentSerializer(TrackTimeSerializer, MaskFieldSerializer):

    # Required
    name = serializers.CharField(
        required=True,
        help_text='Corporation name'
    )
    dependency = serializers.PrimaryKeyRelatedField(
        queryset=models.Dependency.objects.all(),
        required=True,
        help_text='Secondment dependency'
    )
    corporation =  serializers.IntegerField(
        source='corporation.id',
        read_only=True,
        help_text='Secondment dependency corporation'
    )

    class Meta:
        model = models.Secondment
        fields = TrackTimeSerializer.Meta.fields + (
            'name',
            'dependency',
            'corporation',
        )


class SecondmentFilterSerializer(serializers.Serializer):

    name__icontains = serializers.CharField(required=False)

    dependency_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    dependency__corporation_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    created_at__gte = serializers.DateTimeField(required=False)

    created_at__lte = serializers.DateTimeField(required=False)

    order_by = serializers.ChoiceField(
        choices=descent_orders((
            'name',
            'dependency__name',
            'dependency__corporation__name',
            'created_at'
        )),
        required=False
    )


class PositionSerializer(TrackTimeSerializer, MaskFieldSerializer):

    # Required
    name = serializers.CharField(
        required=True,
        help_text='Position name'
    )

    secondment = serializers.PrimaryKeyRelatedField(
        queryset=models.Secondment.objects.all(),
        required=True,
        help_text='Position secondment'
    )

    dependency = serializers.IntegerField(
        source='dependency.id',
        read_only=True,
        help_text='Position dependency'
    )
    corporation = serializers.IntegerField(
        source='corporation.id',
        read_only=True,
        help_text='Position corporation'
    )

    class Meta:
        model = models.Position
        fields = TrackTimeSerializer.Meta.fields + (
            'name',
            'secondment',
            'dependency',
            'corporation',
        )


class PositionFilterSerializer(serializers.Serializer):

    name__icontains = serializers.CharField(required=False)

    secondment_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    secondment__dependency_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    secondment__dependency__corporation_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    created_at__gte = serializers.DateTimeField(required=False)

    created_at__lte = serializers.DateTimeField(required=False)

    order_by = serializers.ChoiceField(
        choices=descent_orders((
            'name',
            'secondment__name'
            'secondment__dependency__name',
            'secondment__dependency__corporation__name',
            'created_at'
        )),
        required=False
    )


class ApplicationSerializer(TrackTimeSerializer, MaskFieldSerializer):

    evaluation = serializers.PrimaryKeyRelatedField(
        read_only=True,
        help_text='Application evaluation'
    )

    # Required
    document = serializers.CharField(
        required=True,
        help_text='Application document'
    )

    date = serializers.DateField(
        required=True,
        help_text='Application document date'
    )

    status = serializers.ChoiceField(
        required=False,
        choices=models.Application.STATUS_CHOICES,
        help_text='Application status'
    )

    candidate = serializers.PrimaryKeyRelatedField(
        queryset=models.Candidate.objects.all(),
        required=True,
        help_text='Application candidate'
    )

    position = serializers.PrimaryKeyRelatedField(
        queryset=models.Position.objects.all(),
        required=True,
        help_text='Application position'
    )

    secondment = serializers.IntegerField(
        source='secondment.id',
        read_only=True,
        help_text='Application position secondment'
    )

    dependency = serializers.IntegerField(
        source='dependency.id',
        read_only=True,
        help_text='Application position dependency'
    )
    corporation = serializers.IntegerField(
        source='corporation.id',
        read_only=True,
        help_text='Application position corporation'
    )

    accepted_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )

    rejected_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )

    archived_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )

    class Meta:
        model = models.Application
        fields = TrackTimeSerializer.Meta.fields + (
            'evaluation',
            'document',
            'date',
            'status',
            'candidate',
            'corporation',
            'dependency',
            'secondment',
            'position',
            'accepted_at',
            'rejected_at',
            'archived_at',
        )


class ApplicationFilterSerializer(serializers.Serializer):

    candidate_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    candidate__name__icontains = serializers.CharField(required=False)

    candidate__last_name__icontains = serializers.CharField(required=False)

    candidate__curp__icontains = serializers.CharField(required=False)

    document__icontains = serializers.CharField(required=False)

    date__gte = serializers.DateField(required=False)

    date__lte = serializers.DateField(required=False)

    status__in = serializers.ListSerializer(
        child=serializers.ChoiceField(
            choices=models.Application.STATUS_CHOICES,
        ),
        required = False
    )

    position__secondment__dependency__corporation_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    position__secondment__dependency_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    position__secondment_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    position_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    created_at__gte = serializers.DateTimeField(required=False)

    created_at__lte = serializers.DateTimeField(required=False)

    order_by = serializers.ChoiceField(
        choices=descent_orders((
            'document',
            'date',
            'status',
            'candidate__last_name',
            'position__name',
            'position__secondment__dependency__corporation__name',
            'position__secondment__dependency__name',
            'position__secondment__name',
            'created_at'
        )),
        required=False
    )