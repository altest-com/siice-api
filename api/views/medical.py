from .evaluation import EvalSectionView

from .. import models
from .. import serializers


class MedicalView(EvalSectionView):
    model_name = 'Medical'
    queryset = models.Medical.objects.all()
    serializer_class = serializers.MedicalSerializer

