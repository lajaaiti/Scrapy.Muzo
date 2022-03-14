import csv

import logging
from unicodedata import name
from unittest import result
from scrapy.crawler import CrawlerProcess
from scrapy.exporters import CsvItemExporter
import scrapy

class MySpider(object):
    def __init__(self) -> None:
        self.file = open('output.tmp', 'wb')
        self.exporter = CsvItemExporter(self.file, str)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        
    def process_item(self, item, spider):
        self.exporter.export(item)
        return item
        
        
class Spid1(scrapy.Spider):
    name = 'spid1'
    
    start_urls = ['https://fr.muzeo.com/recherche/oeuvre/affiche/periode-renaissance/type-cadre-tableau']

    custom_settings = {
        'LOG_LEVEL': logging.warning,
        'ITEM_PIPELINES': {'__main__.MyPipeline': 1},
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEED_EXPORT_FIELDS': ['Titre', 'Prix', 'Delai_De_Fabrication', 'Url_Image'],
        'FEED FORMAT': 'csv',
        'FEED_URI': 'dataScrapy.csv'
    }
    
 
    
    def parse(self, response):
        for result in response.css('div.oeuvre_infos > h3 > a'):
          yield scrapy.Request(url=result.xpath('@href').extract_first(), callback=self.parse_article)
           
    
    def parse_article(self, response):
        
        Titre = response.css('span.title_oeuvre::text').get(),
      
        
        yield {
            'Titre': Titre.strip(),
            
        }     

process = CrawlerProcess(
    {
        "USER_AGENT": "Chrome/41.0.2228.0, Edge/12.10240",
    }
    
)

process.crawl(Spid1)
process.start()
        
          