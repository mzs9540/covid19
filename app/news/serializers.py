from rest_framework import serializers

from core.models import CovidNews


class WhoNewsSerializer(serializers.ModelSerializer):
    """Serialize a news"""

    class Meta:
        model = CovidNews
        fields = ('id', 'title', 'href', 'date')
        read_only_fields = ('id',)


class UpdatesSerializer(serializers.ModelSerializer):
    """Serilaizer for showing updates of different country"""

    class Meta:
        model = None
        fields = '__all__'
        read_only_fields = ('id',)

