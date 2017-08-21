# -*- coding: utf-8 -*-
import scrapy
from herennia.spiders.spiderman import SpiderMan

# http://www.btc38.com/company_notices.html 是个动态网页
# 用 Selenium + PhantomJS 会被视为黑客攻击
# 用 Selenium + FireFox 可行，但是我不想这么做
# 所以还是抓首页的吧
class Btc38Spider(scrapy.Spider):
    name = "btc38"

    def start_requests(self):
        url = SpiderMan.url(self.name)
        yield scrapy.Request(url, headers=SpiderMan.headers)
    
    def parse(self, response):
        return SpiderMan.parse(self.name)(response, with_host=False)

