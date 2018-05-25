# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SelfwoaiduCrawlSimpleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novelId = scrapy.Field()
    novelName = scrapy.Field()
    novelLink = scrapy.Field()

class SelfwoaiduCrawlDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novelId = scrapy.Field()
    novelLink = scrapy.Field()
    novelAuthor = scrapy.Field()
    novelImage = scrapy.Field()
    novelSummary = scrapy.Field()
    novelDownloadInfo = scrapy.Field()
    novelImagePath = scrapy.Field()



