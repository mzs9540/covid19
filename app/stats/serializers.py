from rest_framework import serializers
from core import models


class StatsSerializer(serializers.ModelSerializer):
    """Serilaizer for showing stats of different country"""

    class Meta:
        model = None
        fields = '__all__'
        read_only_fields = ('id',)


class WorldStatsSerializer(serializers.ModelSerializer):
    """Serializer for showing stats """

    class Meta:
        model = models.WorldCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class IndiaStatsSerializer(serializers.ModelSerializer):
    """Serializer for India Table Data"""

    class Meta:
        model = models.IndiaFullCovidStats
        fields = '__all__'
        read_only_fields = ('id',)
