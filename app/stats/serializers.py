from rest_framework import serializers
from core import models


class WorldSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.WorldCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class IndiaSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.IndiaCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class SpainSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.SpainCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class TurkeySerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.TurkeyCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class ItalySerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.ItalyCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class IranSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.IranCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class UkSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.UKCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class UsSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.UsCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class RussiaSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.RussiaCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class UkraineSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.UkraineCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class ChinaSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.ChinaCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class GermanySerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.GermanyCovidStats
        fields = '__all__'
        read_only_fields = ('id',)


class FranceSerializer(serializers.ModelSerializer):
    """Serializer for converting csv file"""

    class Meta:
        model = models.FranceCovidStats
        fields = '__all__'
        read_only_fields = ('id',)
