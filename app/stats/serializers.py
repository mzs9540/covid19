from rest_framework import serializers
from core.models import WorldCovidStats


class CSVSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = WorldCovidStats
        fields = '__all__'
        read_only_fields = ('id',)
