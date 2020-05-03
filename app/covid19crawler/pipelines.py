from scrapy.exporters import CsvItemExporter


class Covid19CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class Covid19NewsCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class IndiaStatsCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class CSVPipeline(object):
    def __init__(self):
        self.files = {}
        self.exporter = None
        self.exporter1 = None

    def open_spider(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        file1 = open('%s.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.files['covid'] = file1
        self.exporter = CsvItemExporter(file)
        self.exporter1 = CsvItemExporter(file1)
        self.exporter.fields_to_export = ['countries', 'total_cases',
                                          'new_cases', 'total_recovered',
                                          'active_cases',
                                          'total_cases_per_million',
                                          'death_per_million', 'total_deaths',
                                          'new_deaths']
        self.exporter1.fields_to_export = ['new_cases', 'total_cases',
                                           'total_deaths', 'new_deaths']
        self.exporter.start_exporting()
        self.exporter1.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.exporter1.finish_exporting()
        file = self.files.pop(spider)
        file1 = self.files.pop('covid')
        file.close()
        file1.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        self.exporter1.export_item(item)
        return item


class CSVNewsPipeline(object):

    def __init__(self):
        self.files = {}
        self.exporter = None

    def open_spider(self, spider):
        file = open('%s.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
