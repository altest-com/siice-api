from rest_framework import serializers
from ._abstracts import TrackTimeSerializer, MaskFieldSerializer
from .. import models


class EvalSectionSerializer(MaskFieldSerializer, TrackTimeSerializer):

    status = serializers.ChoiceField(
        required=False,
        choices=models.EvalSection.STATUS_CHOICES
    )
    result = serializers.CharField(
        required=False,
        allow_blank=True
    )
    passed = serializers.BooleanField(
        required=False,
        allow_null=True
    )
    alert = serializers.CharField(
        required=False,
        allow_blank=True
    )
    started_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    finished_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    alerted_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )

    class Meta:
        fields = TrackTimeSerializer.Meta.fields + (
            'status',
            'result',
            'passed',
            'alert',
            'started_at',
            'finished_at',
            'alerted_at'
        )


class EvaluationSerializer(MaskFieldSerializer, TrackTimeSerializer):

    type = serializers.ChoiceField(
        required=False,
        choices=models.Evaluation.TYPE_CHOICES
    )
    scheduled_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    application = serializers.PrimaryKeyRelatedField(
        queryset=models.Application.objects.all(),
        required=True,
        help_text='Evaluation application'
    )
    socioeconomic = serializers.PrimaryKeyRelatedField(
        queryset=models.Socioeconomic.objects.all(),
        required=True,
        help_text='Socioeconomic evaluation'
    )
    medical = serializers.PrimaryKeyRelatedField(
        queryset=models.Medical.objects.all(),
        required=True,
        help_text='Medical evaluation'
    )
    toxicological = serializers.PrimaryKeyRelatedField(
        queryset=models.Toxicological.objects.all(),
        required=True,
        help_text='Toxicological evaluation'
    )
    psychological = serializers.PrimaryKeyRelatedField(
        queryset=models.Psychological.objects.all(),
        required=True,
        help_text='Psychological evaluation'
    )
    polygraphic = serializers.PrimaryKeyRelatedField(
        queryset=models.Polygraphic.objects.all(),
        required=True,
        help_text='Polygraphic evaluation'
    )

    class Meta:
        model = models.Evaluation
        fields = TrackTimeSerializer.Meta.fields + (
            'type',
            'scheduled_at',
            'application',
            'socioeconomic',
            'medical',
            'toxicological',
            'psychological',
            'polygraphic'
        )
