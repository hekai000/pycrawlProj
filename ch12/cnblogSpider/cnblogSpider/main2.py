# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.cnblogs_spider import CnblogsSpider
if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(CnblogsSpider)
    process.start()