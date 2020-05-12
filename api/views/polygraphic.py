from .evaluation import EvalSectionView

from .. import models
from .. import serializers


class PolygraphicView(EvalSectionView):
    model_name = 'Polygraphic'
    queryset = models.Polygraphic.objects.all()
    serializer_class = serializers.PolygraphicSerializer
