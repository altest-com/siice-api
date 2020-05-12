from rest_framework import serializers
from ._abstracts import (
    TrackTimeSerializer,
    MaskFieldSerializer,
    descent_orders
)
from .. import models


class EvalSectionSerializer(MaskFieldSerializer, TrackTimeSerializer):

    eval_data = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    evaluation = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
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
    scheduled_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    started_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    finished_at = serializers.DateTimeField(
        required=False,
        allow_null=True
    )

    class Meta:
        fields = TrackTimeSerializer.Meta.fields + (
            'eval_data',
            'evaluation',
            'status',
            'result',
            'passed',
            'scheduled_at',
            'started_at',
            'finished_at'
        )


class EvalSectionFilterSerializer(serializers.Serializer):

    status__in = serializers.ListSerializer(
        child=serializers.ChoiceField(
            choices=models.EvalSection.STATUS_CHOICES
        ),
        required=False
    )

    scheduled_at__gte = serializers.DateTimeField(required=False)

    scheduled_at__lte = serializers.DateTimeField(required=False)


class EvaluationSerializer(MaskFieldSerializer, TrackTimeSerializer):

    type = serializers.ChoiceField(
        required=False,
        choices=models.Evaluation.TYPE_CHOICES
    )

    mode = serializers.ChoiceField(
        required=False,
        choices=models.Evaluation.MODE_CHOICES
    )

    resources = serializers.ChoiceField(
        required=False,
        choices=models.Evaluation.RESOURCES_CHOICES
    )

    schema = serializers.ChoiceField(
        required=False,
        choices=models.Evaluation.SCHEMA_CHOICES
    )

    status = serializers.ChoiceField(
        required=False,
        choices=models.Evaluation.STATUS_CHOICES
    )

    reason = serializers.ChoiceField(
        required=False,
        choices=models.Evaluation.REASON_CHOICES
    )

    application = serializers.PrimaryKeyRelatedField(
        queryset=models.Application.objects.all(),
        help_text='Evaluation application'
    )
    socioeconomic = serializers.PrimaryKeyRelatedField(
        read_only=True,
        help_text='Socioeconomic evaluation'
    )
    medical = serializers.PrimaryKeyRelatedField(
        read_only=True,
        help_text='Medical evaluation'
    )
    toxicological = serializers.PrimaryKeyRelatedField(
        read_only=True,
        help_text='Toxicological evaluation'
    )
    psychological = serializers.PrimaryKeyRelatedField(
        read_only=True,
        help_text='Psychological evaluation'
    )
    polygraphic = serializers.PrimaryKeyRelatedField(
        read_only=True,
        help_text='Polygraphic evaluation'
    )

    class Meta:
        model = models.Evaluation
        fields = TrackTimeSerializer.Meta.fields + (
            'type',
            'mode',
            'resources',
            'schema',
            'status',
            'reason',
            'application',
            'socioeconomic',
            'medical',
            'toxicological',
            'psychological',
            'polygraphic'
        )


class EvaluationFilterSerializer(serializers.Serializer):

    type__in = serializers.ListSerializer(
        child=serializers.ChoiceField(
            choices=models.Evaluation.TYPE_CHOICES
        ),
        required=False
    )

    created_at__gte = serializers.DateTimeField(required=False)

    created_at__lte = serializers.DateTimeField(required=False)

    # Related filters

    application__candidate_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    application__candidate__name__icontains = serializers.CharField(
        required=False
    )

    application__candidate__last_name__icontains = serializers.CharField(
        required=False
    )

    application__candidate__curp__icontains = serializers.CharField(
        required=False
    )

    application__document__icontains = serializers.CharField(
        required=False
    )

    application__date__gte = serializers.DateField(
        required=False
    )

    application__date__lte = serializers.DateField(
        required=False
    )

    application__status__in = serializers.ListSerializer(
        child=serializers.ChoiceField(
            choices=models.Application.STATUS_CHOICES,
        ),
        required = False
    )

    application__position__secondment__dependency__corporation_id__in = \
        serializers.ListSerializer(
            child=serializers.IntegerField(),
            required=False
        )

    application__position__secondment__dependency_id__in = \
        serializers.ListSerializer(
            child=serializers.IntegerField(),
            required=False
        )

    application__position__secondment_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    application__position_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    order_by = serializers.ChoiceField(
        choices=descent_orders((
            'type',
            'created_at',
            'application__document',
            'application__date',
            'application__status',
            'application__candidate__curp',
            'application__position_id',
            'application__position__secondment__dependency__corporation_id',
            'application__position__secondment__dependency_id',
            'application__position__secondment_id',
        )),
        required=False
    )


class AlertSerializer(MaskFieldSerializer, TrackTimeSerializer):

    section = serializers.ChoiceField(
        choices=models.Alert.SECTION_CHOICES
    )

    info = serializers.CharField()

    evaluation = serializers.PrimaryKeyRelatedField(
        queryset=models.Evaluation.objects.all(),
        help_text='Alert evaluation'
    )

    class Meta:
        model = models.Alert
        fields = TrackTimeSerializer.Meta.fields + (
            'section',
            'info',
            'evaluation'
        )

