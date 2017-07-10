# -*- coding: utf-8 -*-
import scrapy
from herennia.spiders.spiderman import SpiderMan

class Btc38Spider(scrapy.Spider):
    name = "btc38"

    def start_requests(self):
        url = SpiderMan.url(self.name)
        yield scrapy.Request(url, headers=SpiderMan.headers)
    
    def parse(self, response):
        return SpiderMan.parse(self.name)(response, with_host=False)

