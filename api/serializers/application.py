from rest_framework import serializers
from ._abstracts import TrackTimeSerializer, MaskFieldSerializer
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

    class Meta:
        model = models.Secondment
        fields = TrackTimeSerializer.Meta.fields + (
            'name',
            'dependency'
        )


class PositionSerializer(TrackTimeSerializer, MaskFieldSerializer):

    # Required
    name = serializers.CharField(
        required=True,
        help_text='Position name'
    )

    class Meta:
        model = models.Position
        fields = TrackTimeSerializer.Meta.fields + (
            'name',
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

    year = serializers.IntegerField(
        required=True,
        help_text='Application document year'
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

    corporation = serializers.PrimaryKeyRelatedField(
        queryset=models.Corporation.objects.all(),
        required=True,
        help_text='Application corporation'
    )

    dependency = serializers.PrimaryKeyRelatedField(
        queryset=models.Dependency.objects.all(),
        required=True,
        help_text='Application dependency'
    )

    secondment = serializers.PrimaryKeyRelatedField(
        queryset=models.Secondment.objects.all(),
        required=True,
        help_text='Application secondment'
    )

    position = serializers.PrimaryKeyRelatedField(
        queryset=models.Position.objects.all(),
        required=True,
        help_text='Application position'
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
            'year',
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