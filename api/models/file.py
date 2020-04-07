from django.db import models
from django.conf import settings
from ._abstracts import TrackTimeModel


class Image(TrackTimeModel):

    image = models.ImageField(upload_to=settings.IMAGES_PATH)
    size_bytes = models.IntegerField(blank=True, default=0)
    height = models.IntegerField(blank=True, default=0)
    width = models.IntegerField(blank=True, default=0)