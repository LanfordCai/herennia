# -*- coding: utf-8 -*-
import scrapy
from herennia.items import AnnouncementItem

class YunbiSpider(scrapy.Spider):
    name = "yunbi"
    host = "https://yunbi.zendesk.com"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safar'
                      'i/537.36',
    }

    def start_requests(self):
        url = self.host + "/hc/zh-cn/sections/115001437708-业务公告"
        yield scrapy.Request(url, headers=self.headers)
    
    def parse(self, response):
        # 此处不能用 yield, 否则 scrapyrt 返回的列表里面的 item 都是一样的
        items = []
        for article in response.xpath('//li[@class="article-list-item "]'):
            item = AnnouncementItem()
            item['title'] = article.xpath('./a/text()').extract_first().strip()
            item['link'] = self.host + article.xpath('./a/@href').extract_first()
            items.append(item)
        return items

    