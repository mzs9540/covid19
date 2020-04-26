import csv

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from stats import serializers

from core.models import WorldCovidStats

from core.permissions.permission import PermissionsForAdmin


class CSVParser(APIView):
    """Handle upload of CSV file"""
    parser_classes = (MultiPartParser, )
    authentication_classes = (TokenAuthentication,)
    permission_classes = (PermissionsForAdmin,)

    def post(self, request, *args, **kwargs):
        # to access files
        WorldCovidStats.objects.all().delete()
        with open(f"{request.data['csv']}") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row1 in csv_reader:
                row = row1[1:]
                row = [float(x) for x in row]
                print(row)
                data = {
                    'country': row1[0],
                    'total_case': row[0],
                    'new_case': row[1],
                    'total_recovered': row[2],
                    'active_case': row[3],
                    'cases_per_million': row[4],
                    'deaths_per_million': row[5],
                    'total_death': row[6],
                    'new_death': row[7]
                }
                serializer = serializers.CSVSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        return Response({'received data': request.data})


class WorldStatListView(generics.ListAPIView):
    """Manage World State in the database"""
    serializer_class = serializers.CSVSerializer
    queryset = WorldCovidStats.objects.all()
    permission_classes = (PermissionsForAdmin,)
    authentication_classes = (TokenAuthentication,)
