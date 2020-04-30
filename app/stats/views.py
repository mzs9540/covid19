import csv
from datetime import datetime

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from stats import serializers

from core import models
from core.permissions.permission import PermissionsForStaff


def csv_parser_helper(request, model):
    model.objects.all().delete()
    arr = []
    with open(f"{request.data['csv']}") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data = {
                'date': datetime.strptime(row[0], '%m/%d/%Y').date(),
                'confirmed': int(row[1]),
                'recovered': int(row[2]),
                'deaths': int(row[3]),
            }
            arr.append(data)
    return arr


class CSVParser(APIView):
    """Handle upload of CSV file"""
    parser_classes = (MultiPartParser, )
    authentication_classes = (TokenAuthentication,)
    permission_classes = (PermissionsForStaff,)

    def post(self, request, *args, **kwargs):
        # to access files
        if kwargs['country'] == 'world':
            models.WorldCovidStats.objects.all().delete()
            with open(f"{request.data['csv']}") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row1 in csv_reader:
                    row = row1[1:]
                    row = [float(x) for x in row]
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
                    serializer = serializers.WorldSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
        elif kwargs['country'] == 'india':
            arr = csv_parser_helper(request, models.IndiaCovidStats)
            for data in arr:
                serializer = serializers.IndiaSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'iran':
            arr = csv_parser_helper(request, models.IranCovidStats)
            for data in arr:
                serializer = serializers.IranSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'turkey':
            arr = csv_parser_helper(request, models.TurkeyCovidStats)
            for data in arr:
                serializer = serializers.TurkeySerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'uk':
            arr = csv_parser_helper(request, models.UKCovidStats)
            for data in arr:
                serializer = serializers.UkSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'us':
            arr = csv_parser_helper(request, models.UsCovidStats)
            for data in arr:
                serializer = serializers.UsSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'germany':
            arr = csv_parser_helper(request, models.GermanyCovidStats)
            for data in arr:
                serializer = serializers.GermanySerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'spain':
            arr = csv_parser_helper(request, models.SpainCovidStats)
            for data in arr:
                serializer = serializers.SpainSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'italy':
            arr = csv_parser_helper(request, models.ItalyCovidStats)
            for data in arr:
                serializer = serializers.ItalySerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'ukraine':
            arr = csv_parser_helper(request, models.UkraineCovidStats)
            for data in arr:
                serializer = serializers.UkraineSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'france':
            arr = csv_parser_helper(request, models.FranceCovidStats)
            for data in arr:
                serializer = serializers.FranceSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'russia':
            arr = csv_parser_helper(request, models.RussiaCovidStats)
            for data in arr:
                serializer = serializers.RussiaSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        elif kwargs['country'] == 'china':
            arr = csv_parser_helper(request, models.ChinaCovidStats)
            for data in arr:
                serializer = serializers.ChinaSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        else:
            return Response('Please Provide Valid Country')

        return Response({'received data': request.data})


class StatListView(generics.ListAPIView):
    """Manage World State in the database"""
    permission_classes = (PermissionsForStaff,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.kwargs['stats'] == 'world':
            return models.WorldCovidStats.objects.all()
        elif self.kwargs['stats'] == 'india':
            return models.IndiaCovidStats.objects.all()
        elif self.kwargs['stats'] == 'iran':
            return models.IranCovidStats.objects.all()
        elif self.kwargs['stats'] == 'turkey':
            return models.TurkeyCovidStats.objects.all()
        elif self.kwargs['stats'] == 'uk':
            return models.UKCovidStats.objects.all()
        elif self.kwargs['stats'] == 'us':
            return models.UsCovidStats.objects.all()
        elif self.kwargs['stats'] == 'germany':
            return models.GermanyCovidStats.objects.all()
        elif self.kwargs['stats'] == 'spain':
            return models.SpainCovidStats.objects.all()
        elif self.kwargs['stats'] == 'italy':
            return models.ItalyCovidStats.objects.all()
        elif self.kwargs['stats'] == 'ukraine':
            return models.UkraineCovidStats.objects.all()
        elif self.kwargs['stats'] == 'france':
            return models.FranceCovidStats.objects.all()
        elif self.kwargs['stats'] == 'russia':
            return models.RussiaCovidStats.objects.all()
        elif self.kwargs['stats'] == 'china':
            return models.ChinaCovidStats.objects.all()

    def get_serializer_class(self):
        if self.kwargs['stats'] == 'world':
            return serializers.WorldSerializer
        elif self.kwargs['stats'] == 'india':
            return serializers.IndiaSerializer
        elif self.kwargs['stats'] == 'iran':
            return serializers.IranSerializer
        elif self.kwargs['stats'] == 'turkey':
            return serializers.TurkeySerializer
        elif self.kwargs['stats'] == 'uk':
            return serializers.UkSerializer
        elif self.kwargs['stats'] == 'us':
            return serializers.UsSerializer
        elif self.kwargs['stats'] == 'germany':
            return serializers.GermanySerializer
        elif self.kwargs['stats'] == 'spain':
            return serializers.SpainSerializer
        elif self.kwargs['stats'] == 'italy':
            return serializers.ItalySerializer
        elif self.kwargs['stats'] == 'ukraine':
            return serializers.UkraineSerializer
        elif self.kwargs['stats'] == 'france':
            return serializers.FranceSerializer
        elif self.kwargs['stats'] == 'russia':
            return serializers.RussiaSerializer
        elif self.kwargs['stats'] == 'china':
            return serializers.ChinaSerializer
