from .evaluation import EvalSectionView

from .. import models
from .. import serializers


class PsychologicalView(EvalSectionView):
    model_name = 'Psychological'
    queryset = models.Psychological.objects.all()
    serializer_class = serializers.PsychologicalSerializer


