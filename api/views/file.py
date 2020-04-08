from rest_framework import viewsets

from ._mixins import (
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
)
from .. import models
from .. import serializers


class ImageView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'Image'
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer

    def get_queryset(self):
        return self.queryset


class FileView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'pk'
    model_name = 'File'
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer

    def get_queryset(self):
        return self.queryset
