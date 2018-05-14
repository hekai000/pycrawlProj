# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selfwoaidu_crawl.items import SelfwoaiduCrawlSimpleItem, SelfwoaiduCrawlDetailItem
import urlparse
import re

class SelfwoaiduOrgSpider(CrawlSpider):
    name = 'selfwoaidu_org'
    allowed_domains = ['woaidu.org']

    start_urls = ['http://www.woaidu.org/sitemap_1.html']

    rules = (
         Rule(LinkExtractor(allow=r'sitemap_\d+.html'), callback='parse_book_list', follow=True),
    )
    # rules = (
    #      Rule(LinkExtractor(allow=r'sitemap_1.html'), callback='parse_book_list', follow=True),
    # )
    def parse_book_list(self, response):
        books = response.xpath(".//div[@class='zuo1']/div[@class='sousuolist huisebj'] | .//div[@class='zuo1']/div[@class='sousuolist']")
        page_url = 'http://www.woaidu.org/'
        for book in books:
            novelName = book.xpath("./a/text()").extract_first()
            novelLink = book.xpath("./a/@href").extract_first()
            pattern = re.compile('\d+')
            #去掉空格和换行
            novelLink_s = novelLink.strip().replace('\n','')

            match = pattern.search(novelLink_s)
            novelId = match.group() if match else novelLink_s

            bookListItem = SelfwoaiduCrawlSimpleItem(novelId=novelId, novelName=novelName, novelLink=novelLink)
            yield bookListItem
            novelFullLink = urlparse.urljoin(page_url, novelLink)
            request = scrapy.Request(url=novelFullLink, callback=self.parse_book_detail)
            request.meta['novelLink'] = novelLink
            yield request

    def parse_book_detail(self, response):
        # novelAuthor格式,需要进一步处理
        # 小说作者： 随风萧萧兮
        novelLink = response.meta['novelLink']
        novelAuthor = response.xpath(".//div[@class='xiaoxiao']/text()").extract_first()
        novelImage =  response.xpath(".//div[@class='hong']/img/@src").extract_first()
        novelSummary = response.xpath(".//div[@class='lili']/text()").extract_first()
        novelDownloadInfo = response.xpath(".//div[@class='zizi pcdownload']/a/@href").extract()

        bookDetailItem = SelfwoaiduCrawlDetailItem(novelLink=novelLink, novelAuthor=novelAuthor,novelImage=novelImage,novelSummary=novelSummary,novelDownloadInfo=novelDownloadInfo)
        yield bookDetailItem