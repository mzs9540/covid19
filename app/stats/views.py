import csv
from datetime import datetime

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from scrapy.utils.log import configure_logging

from . import serializers

from core import models
from core.permissions.permission import PermissionsForStaff

from scrapy.crawler import CrawlerRunner

from covid19crawler.spiders.covid19 import Covid19
from twisted.internet import reactor


def csv_parser_helper(request, model):
    serializers.StatsSerializer.Meta.model = model
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


class WorldMap(generics.ListAPIView):
    """Handle upload of CSV file"""
    parser_classes = (MultiPartParser, )
    authentication_classes = (TokenAuthentication,)
    permission_classes = (PermissionsForStaff,)
    serializer_class = serializers.WorldMapSerializer
    queryset = models.WorldMapCovidStats.objects.all()


class CSVParser(APIView):
    """Handle upload of CSV file"""
    parser_classes = (MultiPartParser, )
    authentication_classes = (TokenAuthentication,)
    permission_classes = (PermissionsForStaff,)

    def post(self, request, *args, **kwargs):
        # to access files
        if kwargs['var'] == 'world':
            models.WorldCovidStats.objects.all().delete()
            print(request.data['csv'])
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
                    serializer = serializers.WorldStatsSerializer(data=data)
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

        if self.kwargs['stats'] == 'india':
            self.kwargs['model'] = models.IndiaCovidStats
            return models.IndiaCovidStats.objects.all()

        elif self.kwargs['stats'] == 'iran':
            self.kwargs['model'] = models.IranCovidStats
            return models.IranCovidStats.objects.all()

        elif self.kwargs['stats'] == 'turkey':
            self.kwargs['model'] = models.TurkeyCovidStats
            return models.TurkeyCovidStats.objects.all()

        elif self.kwargs['stats'] == 'uk':
            self.kwargs['model'] = models.UKCovidStats
            return models.UKCovidStats.objects.all()

        elif self.kwargs['stats'] == 'us':
            self.kwargs['model'] = models.UsCovidStats
            return models.UsCovidStats.objects.all()

        elif self.kwargs['stats'] == 'germany':
            self.kwargs['model'] = models.GermanyCovidStats
            return models.GermanyCovidStats.objects.all()

        elif self.kwargs['stats'] == 'spain':
            self.kwargs['model'] = models.SpainCovidStats
            return models.SpainCovidStats.objects.all()

        elif self.kwargs['stats'] == 'italy':
            self.kwargs['model'] = models.ItalyCovidStats
            return models.ItalyCovidStats.objects.all()

        elif self.kwargs['stats'] == 'ukraine':
            self.kwargs['model'] = models.UkraineCovidStats
            return models.UkraineCovidStats.objects.all()

        elif self.kwargs['stats'] == 'france':
            self.kwargs['model'] = models.FranceCovidStats
            return models.FranceCovidStats.objects.all()

        elif self.kwargs['stats'] == 'russia':
            self.kwargs['model'] = models.RussiaCovidStats
            return models.RussiaCovidStats.objects.all()

        elif self.kwargs['stats'] == 'china':
            self.kwargs['model'] = models.ChinaCovidStats
            return models.ChinaCovidStats.objects.all()

    def get_serializer_class(self):
        serializers.StatsSerializer.Meta.model = self.kwargs['model']
        return serializers.StatsSerializer


class IndiaTableView(generics.ListAPIView):
    """Views for Managing India Table Data"""
    queryset = models.IndiaFullCovidStats.objects.all()
    serializer_class = serializers.IndiaStatsSerializer
    permission_classes = (PermissionsForStaff,)
    authentication_classes = (TokenAuthentication,)


class WorldTableView(generics.ListAPIView):
    """Views for Managing India Table Data"""
    queryset = models.WorldCovidStats.objects.all()
    serializer_class = serializers.WorldStatsSerializer
    permission_classes = (PermissionsForStaff,)
    authentication_classes = (TokenAuthentication,)


@api_view(('GET',))
def run_scrapy(request):
    """Views for running all scrapy spyder"""
    runner = CrawlerRunner()
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    d = runner.crawl(Covid19)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    return Response()
