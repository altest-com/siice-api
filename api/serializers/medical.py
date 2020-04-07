from .evaluation import EvalSectionSerializer
from .. import models


class MedicalSerializer(EvalSectionSerializer):
    class Meta:
        model = models.Medical
        fields = EvalSectionSerializer.Meta.fields
