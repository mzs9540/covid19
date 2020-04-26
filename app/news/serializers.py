from rest_framework import serializers

from core.models import CovidNews


class WhoNewsSerializer(serializers.ModelSerializer):
    """Serialize a news"""

    class Meta:
        model = CovidNews
        fields = ('id', 'title', 'href', 'date')
        read_only_fields = ('id',)
