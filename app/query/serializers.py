from rest_framework import serializers

from core import models


class Covid19QueryRepliesSerializer(serializers.ModelSerializer):
    """Serializer for Query Model"""

    query = serializers.PrimaryKeyRelatedField(queryset=models.Covid19Query.objects.all())

    class Meta:
        model = models.Covid19QueryReplies
        fields = ('id', 'reply', 'posted_at', 'query', 'user')
        read_only_fields = ('id',)


class Covid19QuerySerializer(serializers.ModelSerializer):
    """Serializer for Query Model"""

    class Meta:
        model = models.Covid19Query
        fields = ('id', 'query', 'admin_reply', 'posted_at',)
        read_only_fields = ('id',)


class Covid19QueryDetailsSerializer(Covid19QuerySerializer):
    """Serializer for Query Model"""

    query_replies = Covid19QueryRepliesSerializer(read_only=True, many=True)

    class Meta(Covid19QuerySerializer.Meta):
        fields = ('id', 'query', 'admin_reply', 'posted_at', 'query_replies')

