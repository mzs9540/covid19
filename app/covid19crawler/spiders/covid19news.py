from datetime import datetime, timedelta

import scrapy
from ..items import Covid19NewsCrawlerItem
from core.models import CovidNews


def to_num(value):
    if value == 'N/A':
        value = '0,0'
    return float(value.replace(',', ''))


class FirstSpider(scrapy.Spider):

    name = 'news'

    start_urls = [
        "https://www.who.int/emergencies/diseases/"
        "novel-coronavirus-2019/media-resources/news"
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'covid19crawler.pipelines.Covid19NewsCrawlerPipeline': 400,
            'covid19crawler.pipelines.CSVNewsPipeline': 500,
        }
    }

    def parse(self, response):
        t = response.xpath('//*[@id="PageContent_C003_Col01"]/div/div/a')
        title = []
        href = []
        date = []

        for data in t.css('.text-underline::text'):
            title.append(data.get())

        for data in t.css('.sub-title::text'):
            print(data.get(), 'khusiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            date.append(datetime.strptime(
                "-".join(data.get().replace(',', ' ').split()[:3]),
                '%d-%B-%Y').date())

        for data in t.xpath('@href'):
            href.append(data.get())

        length = min(len(date), len(href), len(title))
        today = datetime.today().date()
        yesterday = today - timedelta(days=1)
        for i in range(length):
            items = Covid19NewsCrawlerItem()
            if yesterday == date[i]:
                print(date[i], 'hooooooolaaa')
            it, created = CovidNews.objects.get_or_create(
                title=title[i],
                date=date[i],
                defaults={'href': href[i]})
            items['title'] = title[i]
            items['href'] = href[i]
            items['date'] = date[i]
            yield items
