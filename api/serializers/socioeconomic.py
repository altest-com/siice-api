from .evaluation import EvalSectionSerializer
from .. import models
from rest_framework import serializers


class SocioeconomicSerializer(EvalSectionSerializer):

    digi_entry = serializers.ChoiceField(
        choices=models.Socioeconomic.DIGI_ENTRY_CHOICES,
        required=False,
        allow_blank=True
    )

    digi_date = serializers.DateField(
        required=False,
        allow_null=True
    )

    digi_id_type = serializers.ChoiceField(
        required=False,
        choices=models.Socioeconomic.ID_TYPE_CHOICES,
        allow_blank=True
    )

    digi_id_number = serializers.CharField(
        required=False,
        allow_null=True
    )

    digi_image = serializers.PrimaryKeyRelatedField(
        queryset=models.Image.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = models.Socioeconomic
        fields = EvalSectionSerializer.Meta.fields + (
            'digi_entry',
            'digi_date',
            'digi_id_type',
            'digi_id_number',
            'digi_image'
        )
