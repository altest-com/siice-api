from .evaluation import EvalSectionSerializer
from .. import models


class PolygraphicSerializer(EvalSectionSerializer):
    class Meta:
        model = models.Polygraphic
        fields = EvalSectionSerializer.Meta.fields
