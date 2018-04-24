# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

from firstSpider.DataOutput import DataOutput
from firstSpider.HTMLDownloader import HTMLDownloader
from firstSpider.MyHTMLParser import MyHTMLParser
from firstSpider.URLManager import URLManager

class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HTMLDownloader()
        self.parser = MyHTMLParser()
        self.output = DataOutput()


    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while (self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print "已经抓取了%s个连接" % self.manager.old_url_size()
            except Exception as e:
                print "crawl failed"
            self.output.output_html()

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")