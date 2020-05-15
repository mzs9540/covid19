from datetime import datetime

import scrapy
from ..items import Covid19CrawlerItem, FullStatsCrawlerItem
from core.models import WorldMapCovidStats, WorldCovidStats


def to_num(value):
    if value == 'N/A' or value.isspace():
        return 0
    return float(value.replace(',', ''))


def is_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


class FirstSpider(scrapy.Spider):
    name = 'covid19'
    start_urls = [
        'https://www.worldometers.info/coronavirus/'
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'covid19crawler.pipelines.Covid19CrawlerPipeline': 300,
            'covid19crawler.pipelines.CSVPipeline': 500,
        }
    }

    def parse(self, response):
        def item(i):
            items = Covid19CrawlerItem()
            items['countries'] = countries[i]
            items['total_cases'] = total_cases[i]
            items['new_cases'] = new_cases[i]
            items['total_recovered'] = total_recovered[i]
            items['active_cases'] = active_cases[i]
            items['total_cases_per_million'] = total_cases_per_million[i]
            items['death_per_million'] = death_per_million[i]
            items['total_deaths'] = total_deaths[i]
            items['new_deaths'] = new_deaths[i]

            return items

        t = response.css('table')
        countries = []
        total_cases = []
        new_cases = []
        total_deaths = []
        total_recovered = []
        active_cases = []
        total_cases_per_million = []
        death_per_million = []
        new_deaths = []
        for data in t.css('td:nth-child(2) a::text').extract()[8:213]:
            countries.append(data)

        for data in t.css('td:nth-child(3)')[8:213]:
            value = data.css('::text').get(default='0')
            total_cases.append(to_num(value))

        for data in t.css('td:nth-child(4)')[8:213]:
            value = "".join(data.css('::text').get(default='0'))
            new_cases.append(to_num(value))

        for data in t.css('td:nth-child(5)')[8:213]:
            value = data.css('::text').get(default=0)
            if value == ' ' or value == '  ':
                value = '0'
            total_deaths.append(to_num(value))

        for data in t.css('td:nth-child(6)')[8:213]:
            value = "".join(data.css('::text').get(default='0'))
            new_deaths.append(to_num(value))

        for data in t.css('td:nth-child(7)')[8:213]:
            value = "".join(data.css('::text').get(default='0'))
            total_recovered.append(to_num(value))

        for data in t.css('td:nth-child(8)')[8:213]:
            value = "".join(data.css('::text').get(default='0'))
            active_cases.append(to_num(value))

        for data in t.css('td:nth-child(10)')[8:213]:
            value = "".join(data.css('::text').get(default='0'))
            total_cases_per_million.append(to_num(value))

        for data in t.css('td:nth-child(11)')[8:213]:
            value = "".join(data.css('::text').get(default='0'))
            death_per_million.append(to_num(value))
            
        # countries = countries[8:221]
        # total_cases = total_cases[8:221]
        # new_cases = new_cases[8:221]
        # total_deaths = total_deaths[8:221]
        # total_recovered = total_recovered[8:221]
        # active_cases = active_cases[8:221]
        # total_cases_per_million = total_cases_per_million[8:221]
        # death_per_million = death_per_million[8:221]
        # new_deaths = new_deaths[8:221]

        WorldCovidStats.objects.all().delete()
        for i in range(205):
            items = item(i)
            WorldCovidStats.objects.create(country=items['countries'],
                                           total_case=items['total_cases'],
                                           new_case=items['new_cases'],
                                           total_recovered=items['total_recovered'],
                                           active_case=items['active_cases'],
                                           cases_per_million=items['total_cases_per_million'],
                                           deaths_per_million=items['death_per_million'],
                                           total_death=items['total_deaths'],
                                           new_death=items['new_deaths'])

        for i in range(len(total_cases)):
            items = item(i)
            yield items


class FullCovid19Stats(scrapy.Spider):
    name = 'FullCovid19Stats'
    start_urls = [
        'https://raw.githubusercontent.com/datasets/covid-19/'
        'master/data/time-series-19-covid-combined.csv'
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'covid19crawler.pipelines.Covid19CrawlerPipeline': 300,
            'covid19crawler.pipelines.CSVNewsPipeline': 500,
        }
    }

    def parse(self, response):
        items = FullStatsCrawlerItem()
        t = response.xpath('/html/body//text()').extract()
        t = t[0].split('\r\n')
        t = [x for x in t if '2020-05-04' in x]
        t = [x for x in t if is_number(x.split(',')[3]) and is_number(x.split(',')[4])]
        WorldMapCovidStats.objects.all().delete()
        for i in range(len(t)):
            temp = t[i].split(',')
            items['date'] = datetime.strptime(temp[0], '%Y-%m-%d').date()
            items['country'] = temp[1]
            items['province'] = temp[2]
            items['lat'] = temp[3]
            items['lon'] = temp[4]
            items['confirmed'] = temp[5] if temp[5] != '' else 0
            items['recovered'] = temp[6] if temp[6] != '' else 0
            items['deaths'] = temp[7] if temp[7] != '' else 0
            WorldMapCovidStats.objects.create(
                **items
            )
            yield items
