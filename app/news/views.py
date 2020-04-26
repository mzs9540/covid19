from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from core.models import CovidNews
from core.permissions.permission import PermissionsForAdmin
from news import serializers


class WhoNewsViewSet(viewsets.ModelViewSet):
    """Manage News in the database"""
    serializer_class = serializers.WhoNewsSerializer
    queryset = CovidNews.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (PermissionsForAdmin,)
