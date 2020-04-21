from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Evaluation
from .services import fill_evaluation


@receiver(pre_save, sender=Evaluation)
def evaluation_pre_save(sender, instance: Evaluation, **kwargs):
    if instance is not None:
        fill_evaluation(instance)
