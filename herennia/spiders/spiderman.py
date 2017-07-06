# -*- coding: utf-8 -*-
import scrapy
from herennia.items import AnnouncementItem

class SpiderMan:
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/'
                '537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safar'
                'i/537.36',
        'Accept-Language': 'zh-cn'
    }

    okcoin_configs = {
        "name": "okcoin",
        "host": "https://www.okcoin.cn",
        "announcement_page": "/service.html",
        "announcement_xpath": '//span[@class="spanOne"]',
        "title_xpath": './a[@class="lightblue3 fontsize-14"]/text()',
        "link_xpath": './a[@class="lightblue3 fontsize-14"]/@href' 
    }
    
    huobi_configs = {
        "name": "huobi",
        "host": "https://www.huobi.com",
        "announcement_page": "/p/content/notice",
        "announcement_xpath": '//h4[@class="tit"]',
        "title_xpath": "./a/text()",
        "link_xpath": "./a/@href"
    }

    yunbi_configs = {
        "name": "yunbi",
        "host": "https://yunbi.zendesk.com",
        "announcement_page": "/hc/zh-cn/sections/115001437708-业务公告",
        "announcement_xpath": '//li[@class="article-list-item "]',
        "title_xpath": "./a/text()",
        "link_xpath": "./a/@href"
    }

    chbtc_configs = {
        "name": "chbtc",
        "host": "https://www.chbtc.com",
        "announcement_page": "/i/blog?type=proclamation",
        "announcement_xpath": '//article[@class="envor-post"]',
        "title_xpath": './header/h3/a/text()',
        "link_xpath": './header/h3/a/@href'
    }
    
    @classmethod
    def configurations(cls, name):
        if name == "huobi":
            return cls.huobi_configs
        elif name == "yunbi":
            return cls.yunbi_configs
        elif name == "chbtc":
            return cls.chbtc_configs
        elif name == "okcoin":
            return cls.okcoin_configs

    @classmethod
    def url(cls, name):
        configs = cls.configurations(name)
        return configs["host"] + configs["announcement_page"]

    @classmethod
    def parse(cls, name):
        configs = cls.configurations(name)
        def _parse(response, with_host=True):
            items = []
            for article in response.xpath(configs["announcement_xpath"]):
                item = AnnouncementItem()
                item["title"] = article.xpath(configs["title_xpath"]).extract_first().strip()
                if with_host: 
                    item["link"] = configs["host"] + article.xpath(configs["link_xpath"]).extract_first()
                else:
                    item["link"] = article.xpath(configs["link_xpath"]).extract_first()
                items.append(item)
            return items
        return _parse


        
        

