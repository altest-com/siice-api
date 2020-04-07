from .evaluation import EvalSectionSerializer
from .. import models


class PsychologicalSerializer(EvalSectionSerializer):
    class Meta:
        model = models.Psychological
        fields = EvalSectionSerializer.Meta.fields
