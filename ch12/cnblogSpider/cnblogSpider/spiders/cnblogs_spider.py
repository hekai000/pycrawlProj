# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sys
reload(sys)
sys.path.append("..")
sys.setdefaultencoding("utf-8")
from cnblogSpider.items import CnblogspiderItem


class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/qiyeboy/default.html?page=1"]
    def parse(self, response):
        papers = response.xpath(".//*[@class='day']")
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postCon']/div/text()").extract()[0]
            #print str(url).encode(encoding='utf-8'), str(title).encode(encoding='utf-8'), str(time).encode(encoding='utf-8'), str(content).encode(encoding='utf-8')
            #print url, title, time, content
            item = CnblogspiderItem(url=url, title=title, time=time, content=content)
            request = scrapy.Request(url=url, callback=self.parse_body)
            request.meta['item'] = item
            yield request
        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)
    def parse_body(self, response):
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        item['cimages_urls'] = body.xpath('.//img/@src').extract()
        yield item