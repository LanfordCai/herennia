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

    btc9_configs = {
        "name": "btc9",
        "host": "https://www.btc9.com",
        "announcement_page": "/Art/index/id/1.html",
        "announcement_xpath": '//li[@class="list-group-item"]',
        "title_xpath": './a/text()',
        "link_xpath": './a/@href' 
    }

    bter_configs = {
        "name": "bter",
        "host": "https://bter.com",
        "announcement_page": "/articlelist/ann",
        "announcement_xpath": '//div[@class="latnewslist"]/div[@class="entry"]',
        "title_xpath": './a/h3/text()',
        "link_xpath": './a/@href'
    }

    btc38_configs = {
        "name": "btc38",
        "host": "http://www.btc38.com",
        "announcement_page": "",
        "announcement_xpath": '//div[@class="notice"]/ul/li',
        "title_xpath": './a/em/text()',
        "link_xpath": './a/@href'
    }

    jubi_configs = {
        "name": "jubi",
        "host": "https://www.jubi.com",
        "announcement_page": "/gonggao/",
        "announcement_xpath": '//div[@class="new_list"]/ul/li',
        "title_xpath": './a[@class="title"]/text()',
        "link_xpath": './a[@class="title"]/@href' 
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
        elif name == "jubi":
            return cls.jubi_configs
        elif name == "btc38":
            return cls.btc38_configs
        elif name == "bter":
            return cls.bter_configs
        elif name == "btc9":
            return cls.btc9_configs

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


        
        

