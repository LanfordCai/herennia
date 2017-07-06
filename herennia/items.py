# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnnouncementItem(scrapy.Item):
    # 公告标题
    title = scrapy.Field()
    # 公告链接
    link = scrapy.Field()


