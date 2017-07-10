# -*- coding: utf-8 -*-
import scrapy
from herennia.spiders.spiderman import SpiderMan

class Btc38Spider(scrapy.Spider):
    name = "btc38"

    headers = SpiderMan.headers

    def start_requests(self):
        url = SpiderMan.url(self.name)
        yield scrapy.Request(url, headers=self.headers)
    
    def parse(self, response):
        return SpiderMan.parse(self.name)(response)

