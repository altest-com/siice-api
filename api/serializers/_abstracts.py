from rest_framework import serializers


class MaskFieldSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(MaskFieldSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class TrackTimeSerializer:
    created_at = serializers.DateTimeField(
        read_only=True,
        help_text='Date and time when instance was created'
    )
    updated_at = serializers.DateTimeField(
        read_only=True,
        help_text='Date and time when instance was updated'
    )

    class Meta:
        fields = (
            'id',
            'created_at',
            'updated_at'
        )
