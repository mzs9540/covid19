from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication

from core import models
from core.permissions.permission import PermissionsForStaff
from news import serializers


class WhoNewsViewSet(viewsets.ModelViewSet):
    """Manage News in the database"""
    serializer_class = serializers.WhoNewsSerializer
    queryset = models.CovidNews.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (PermissionsForStaff,)


class UpdatesListView(generics.ListAPIView):
    """Manage Update of India in the database"""
    permission_classes = (PermissionsForStaff,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.kwargs['news'] == 'india':
            self.kwargs['model'] = models.IndiaCovid19Update
            return models.IndiaCovid19Update.objects.all()

    def get_serializer_class(self):
        serializers.UpdatesSerializer.Meta.model = self.kwargs['model']
        return serializers.UpdatesSerializer
