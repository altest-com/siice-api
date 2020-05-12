from .evaluation import EvalSectionView

from .. import models
from .. import serializers


class ToxicologicalView(EvalSectionView):
    model_name = 'Toxicological'
    queryset = models.Toxicological.objects.all()
    serializer_class = serializers.ToxicologicalSerializer
