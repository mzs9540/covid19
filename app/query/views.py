from core import models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from query import serializers
from rest_framework.response import Response


class Covid19QueryView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.Covid19QuerySerializer
    queryset = models.Covid19Query.objects.all()

    def get_queryset(self):
        return models.Covid19Query.objects.filter(
            user=self.request.user
        )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.Covid19QueryDetailsSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class Covid19QueryRepliesView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.Covid19QueryRepliesSerializer
    queryset = models.Covid19QueryReplies.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
