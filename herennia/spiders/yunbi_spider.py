# -*- coding: utf-8 -*-
import scrapy
from herennia.spiders.spiderman import SpiderMan

class YunbiSpider(scrapy.Spider):
    name = "yunbi"

    headers = SpiderMan.headers

    def start_requests(self):
        url = SpiderMan.url(self.name)
        yield scrapy.Request(url, headers=self.headers)
    
    def parse(self, response):
        return SpiderMan.parse(self.name)(response)

    