from ._abstracts import TrackTimeModel
from django.db import models


class EvalSection(TrackTimeModel):

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_FINISHED = 'finished'

    STATUS_CHOICES = [
        (STATUS_CREATED, 'created'),
        (STATUS_STARTED, 'started'),
        (STATUS_FINISHED, 'finished')
    ]

    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED
    )

    result = models.TextField(blank=True, default='')

    passed = models.BooleanField(blank=True, null=True)

    scheduled_at = models.DateTimeField(
        null=True,
        blank=True
    )

    started_at = models.DateTimeField(
        null=True,
        blank=True
    )

    finished_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Evaluation(TrackTimeModel):

    TYPE_ENTRANT = 'entrant'
    TYPE_REENTRANT = 'reentrant'
    TYPE_PERMANENCE = 'permanence'
    TYPE_PROMOTION = 'promotion'

    TYPE_CHOICES = [
        (TYPE_ENTRANT, 'entrant'),
        (TYPE_REENTRANT, 'reentrant'),
        (TYPE_PERMANENCE, 'permanence'),
        (TYPE_PROMOTION, 'promotion'),
    ]

    MODE_ORDINARY = 'ordinary'
    MODE_EXTRA = 'extra'
    MODE_REPEAT = 'repeat'

    MODE_CHOICES = [
        (MODE_ORDINARY, 'ordinary'),
        (MODE_EXTRA, 'extra'),
        (MODE_REPEAT, 'repeat')
    ]

    RESOURCES_FORTASEG = 'fortaseg'
    RESOURCES_FASP = 'fasp'
    RESOURCES_OTHER = 'other'

    RESOURCES_CHOICES = [
        (RESOURCES_FORTASEG, 'fortaseg'),
        (RESOURCES_FASP, 'fasp'),
        (RESOURCES_OTHER, 'other')
    ]

    SCHEMA_INTEGRAL = 'integral'
    SCHEMA_DIFFERENTIATED = 'differentiated'
    SCHEMA_FILTER = 'filter'

    SCHEMA_CHOICES = [
        (SCHEMA_INTEGRAL, 'integral'),
        (SCHEMA_DIFFERENTIATED, 'differentiated'),
        (SCHEMA_FILTER, 'filter')
    ]

    STATUS_CREATED = 'created'
    STATUS_ISE_AUTH_PENDING = 'ise_auth_pending'
    STATUS_INT_AUTH_PENDING = 'int_auth_pending'
    STATUS_SCHEDULE_PENDING = 'schedule_pending'
    STATUS_SCHEDULED = 'schedule_pending'
    STATUS_DONT_EVAL = 'dont_eval'
    STATUS_NOT_EVALUABLE = 'not_evaluable'

    STATUS_CHOICES = [
        (STATUS_CREATED, 'created'),
        (STATUS_ISE_AUTH_PENDING, 'ise_auth_pending'),
        (STATUS_INT_AUTH_PENDING, 'int_auth_pending'),
        (STATUS_SCHEDULE_PENDING, 'schedule_pending'),
        (STATUS_SCHEDULED, 'schedule_pending'),
        (STATUS_DONT_EVAL, 'dont_eval'),
        (STATUS_NOT_EVALUABLE, 'not_evaluable')
    ]

    REASON_NONE = 'none'
    REASON_PERIODIC = 'periodic'
    REASON_TRACKING = 'tracking'

    REASON_CHOICES = [
        (REASON_NONE, 'none'),
        (REASON_PERIODIC, 'periodic'),
        (REASON_TRACKING, 'tracking')
    ]

    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        default=TYPE_ENTRANT
    )

    mode = models.CharField(
        max_length=255,
        choices=MODE_CHOICES,
        default=MODE_ORDINARY
    )

    resources = models.CharField(
        max_length=255,
        choices=RESOURCES_CHOICES,
        default=RESOURCES_FORTASEG
    )

    schema = models.CharField(
        max_length=255,
        choices=SCHEMA_CHOICES,
        default=SCHEMA_INTEGRAL
    )

    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED
    )

    reason = models.CharField(
        max_length=255,
        choices=REASON_CHOICES,
        default=REASON_NONE
    )

    application = models.OneToOneField(
        'Application',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    socioeconomic = models.OneToOneField(
        'Socioeconomic',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    medical = models.OneToOneField(
        'Medical',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    toxicological = models.OneToOneField(
        'Toxicological',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    psychological = models.OneToOneField(
        'Psychological',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )

    polygraphic = models.OneToOneField(
        'Polygraphic',
        on_delete=models.CASCADE,
        related_name='evaluation'
    )


class Alert(TrackTimeModel):

    SECTION_SOCIOECONOMIC = 'socioeconomic'
    SECTION_MEDICAL = 'medical'
    SECTION_POLYGRAPHIC = 'polygraphic'
    SECTION_PSYCHOLOGICAL = 'psychological'
    SECTION_TOXICOLOGICAL = 'toxicological'

    SECTION_CHOICES = [
        (SECTION_SOCIOECONOMIC, 'socioeconomic'),
        (SECTION_MEDICAL, 'medical'),
        (SECTION_POLYGRAPHIC, 'polygraphic'),
        (SECTION_PSYCHOLOGICAL, 'psychological'),
        (SECTION_TOXICOLOGICAL, 'toxicological'),
    ]

    evaluation = models.ForeignKey(
        'Evaluation',
        on_delete=models.CASCADE,
        related_name='alerts'
    )

    info = models.TextField()

    section = models.CharField(max_length=64, choices=SECTION_CHOICES)

