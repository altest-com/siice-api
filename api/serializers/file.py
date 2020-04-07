from rest_framework import serializers
from ._abstracts import TrackTimeSerializer, MaskFieldSerializer
from .. import models


class ImageSerializer(TrackTimeSerializer, MaskFieldSerializer):

    size_bytes = serializers.IntegerField(read_only=True)
    height = serializers.IntegerField(read_only=True)
    width = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Image
        fields = TrackTimeSerializer.Meta.fields + (
            'image',
            'size_bytes',
            'height',
            'width'
        )
