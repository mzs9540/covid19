import scrapy


class Covid19CrawlerItem(scrapy.Item):
    countries = scrapy.Field()
    total_recovered = scrapy.Field()
    active_cases = scrapy.Field()
    total_cases_per_million = scrapy.Field()
    death_per_million = scrapy.Field()
    new_cases = scrapy.Field()
    total_cases = scrapy.Field()
    total_deaths = scrapy.Field()
    new_deaths = scrapy.Field()


class Covid19NewsCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
