from .evaluation import EvalSectionView

from .. import models
from .. import serializers


class SocioeconomicView(EvalSectionView):
    model_name = 'Socioeconomic'
    queryset = models.Socioeconomic.objects.all()
    serializer_class = serializers.SocioeconomicSerializer

