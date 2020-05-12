from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Evaluation
from .services import fill_evaluation


@receiver(pre_save, sender=Evaluation)
def evaluation_pre_save(sender, instance: Evaluation, **kwargs):
    if instance is not None:
        fill_evaluation(instance)


@receiver(post_save, sender=Evaluation)
def evaluation_post_save(
    sender,
    instance: Evaluation,
    created: bool = False,
    **kwargs
):
    if instance is not None and created:
        if instance.status == Evaluation.STATUS_CREATED:
            candidate = instance.application.candidate
            prev_evaluations = Evaluation.objects.filter(
                application__candidate_id=candidate.id
            )
            if len(prev_evaluations):
                instance.status = Evaluation.STATUS_INT_AUTH_PENDING
            else:
                instance.status = Evaluation.STATUS_ISE_AUTH_PENDING

            instance.save()
