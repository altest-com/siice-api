from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import (
    Evaluation,
    Socioeconomic,
    Medical,
    Polygraphic,
    Psychological,
    Toxicological
)

sections = [{
    'field': 'socioeconomic',
    'model': Socioeconomic
}, {
    'field': 'medical',
    'model': Medical
}, {
    'field': 'psychological',
    'model': Psychological
}, {
    'field': 'polygraphic',
    'model': Polygraphic
}, {
    'field': 'toxicological',
    'model': Toxicological
}]


@receiver(pre_save, sender=Evaluation)
def evaluation_pre_save(sender, instance: Evaluation, **kwargs):
    if instance is not None:
        for section in sections:
            if not hasattr(instance, section['field']):
                setattr(
                    instance,
                    section['field'],
                    section['model'].objects.create()
                )
