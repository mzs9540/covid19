import scrapy
from ..items import Covid19NewsCrawlerItem


def to_num(value):
    if value == 'N/A':
        value = '0,0'
    return float(value.replace(',', ''))


class FirstSpider(scrapy.Spider):

    name = 'news'

    start_urls = [
        'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news'
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'covid19crawler.pipelines.Covid19NewsCrawlerPipeline': 400,
            'covid19crawler.pipelines.CSVNewsPipeline': 500,
        }
    }

    def parse(self, response):
        items = Covid19NewsCrawlerItem()
        t = response.xpath('//*[@id="PageContent_C003_Col01"]/div/div/a')
        title = []
        href = []

        for data in t.css('.text-underline::text'):

            title.append(data.get())

        print(len(title), 'hooooolaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        for data in t.xpath('@href'):
            href.append(data.get())

        for i in range(len(t)):
            items['title'] = title[i]
            items['href'] = href[i]
            yield items
