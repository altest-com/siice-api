from .evaluation import EvalSectionSerializer
from .. import models


class ToxicologicalSerializer(EvalSectionSerializer):
    class Meta:
        model = models.Toxicological
        fields = EvalSectionSerializer.Meta.fields
