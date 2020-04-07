from .evaluation import EvalSectionSerializer
from .. import models


class SocioeconomicSerializer(EvalSectionSerializer):
    class Meta:
        model = models.Socioeconomic
        fields = EvalSectionSerializer.Meta.fields
