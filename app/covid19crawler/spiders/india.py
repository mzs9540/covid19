from datetime import datetime, timedelta

import scrapy
from ..items import Covid19NewsCrawlerItem, IndiaStatCrawlerItem, IndiaUpdateCrawlerItem
from core.models import IndiaFullCovidStats, IndiaCovid19Update


def to_num(value):
    if value == 'N/A':
        value = '0,0'
    return float(value.replace(',', ''))


class IndiaCovid19Stats(scrapy.Spider):

    name = 'IndiaStats'

    start_urls = [
        "https://www.mygov.in/corona-data/covid19-statewise-status/"
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'covid19crawler.pipelines.IndiaStatsCrawlerPipeline': 400,
        }
    }

    def parse(self, response):
        confirmed = response.css('.field-name-field-total-confirmed-indians .even::text').extract()
        state = response.css('.field-type-list-text .even::text').extract()
        recovered = response.css('.field-name-field-cured .even::text').extract()
        deaths = response.css('.field-name-field-deaths .even::text').extract()
        IndiaFullCovidStats.objects.all().delete()
        for i in range(len(state)):
            items = IndiaStatCrawlerItem()
            IndiaFullCovidStats.objects.create(
                state=state[i],
                total_death=deaths[i],
                total_case= confirmed[i],
                total_recovered= recovered[i])
            items['state'] = state[i]
            items['confirmed'] = confirmed[i]
            items['recovered'] = recovered[i]
            items['deaths'] = deaths[i]
            yield items


class IndiaCovid19Updates(scrapy.Spider):

    name = 'IndiaUpdates'

    start_urls = [
        "https://www.mygov.in/covid-19/",
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'covid19crawler.pipelines.IndiaStatsCrawlerPipeline': 400,
        }
    }

    def parse(self, response):
        t = response.css('.stretched-link')
        t1 = t.css('::text').extract()
        title = []
        date = []
        href = response.css('.stretched-link::attr(href)').extract()

        for i in range(0, len(t1), 2):
            title.append(t1[i])

        for i in range(1, len(t1), 2):
            try:
                dat = datetime.strptime(t1[i], '%Y-%m-%d').date()
                print(dat)
                date.append(dat)
            except (ValueError, TypeError):
                dat = datetime.strptime(t1[i], '%d-%m-%Y').date()
                print(dat)
                date.append(dat)

        for i in range(20):
            it, created = IndiaCovid19Update.objects.get_or_create(
                title=title[i],
                date=date[i],
                defaults={'href': href[i]})
            items = IndiaUpdateCrawlerItem()
            items['title'] = title[i]
            items['date'] = date[i]
            items['href'] = href[i]
            yield items
