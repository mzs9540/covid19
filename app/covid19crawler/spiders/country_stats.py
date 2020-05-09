from datetime import datetime, timedelta

import scrapy
from ..items import StatsCrawlerItem
from core import models


def to_num(value):
    if value == 'N/A':
        value = '0,0'
    return float(value.replace(',', ''))


class IndiaCovid19Stats(scrapy.Spider):

    name = 'CountryStats'

    start_urls = [
        "https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv"
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'covid19crawler.pipelines.IndiaStatsCrawlerPipeline': 400,
        }
    }

    def parse(self, response):
        t = response.css('.js-file-line::text').extract()[-180:]
        temp_arr = ['India', 'US', 'Ukraine', 'Spain', 'Turkey',
                    'Russia', 'Italy', 'Iran', 'Germany', 'France', 'China']
        countries = {}
        for item in t:
            temp = item.replace("\r", "").split(',')
            if temp[1] in temp_arr:
                st = temp.pop(1)
                countries[st] = temp

        for model in [models.ChinaCovidStats,
                      models.UsCovidStats,
                      models.GermanyCovidStats,
                      models.ItalyCovidStats,
                      models.TurkeyCovidStats,
                      models.RussiaCovidStats,
                      models.UkraineCovidStats,
                      models.IranCovidStats,
                      models.FranceCovidStats,
                      models.SpainCovidStats,
                      models.IndiaCovidStats
                      ]:
            index = str(model.objects.first()).split(' ')[0]
            print(index)
            if model.objects.last().date != datetime.strptime(countries[index][0], '%Y-%m-%d').date():
                model.objects.get_or_create(
                    confirmed=countries[index][1],
                    recovered=countries[index][2],
                    deaths=countries[index][3],
                    defaults={
                        'date': datetime.strptime(countries[index][0], '%Y-%m-%d').date(),
                    }
                )
                model.objects.first().delete()
