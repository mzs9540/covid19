from rest_framework import serializers
from core import models


class StatsSerializer(serializers.ModelSerializer):
    """Serilaizer for showing stats of different country"""

    class Meta:
        model = None
        fields = '__all__'
        read_only_fields = ('id',)
