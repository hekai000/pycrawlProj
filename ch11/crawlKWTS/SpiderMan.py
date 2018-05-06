# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

from crawlKWTS.DataOutput import DataOutput
from crawlKWTS.HTMLDownloader import HTMLDownloader
from crawlKWTS.MyHTMLParser import MyHTMLParser

class SpiderMan(object):
    def __init__(self):
        self.downloader = HTMLDownloader()
        self.parser = MyHTMLParser()
        self.output = DataOutput()


    def crawl(self, root_url):
        content = self.downloader.download(root_url)
        print content
        for info in self.parser.get_kw_cat(content):
            print info
            detail_url = 'http://ts.kuwo.cn/service/getlist.v31.php?act=detail&id=%s' % info['id']
            content = self.downloader.download(detail_url)
            details = self.parser.get_kw_detail(content)
            print detail_url
            print "3333333333"
            print details
            print "4444444444"
            self.output.output_html(self.output.filepath, details)
        self.output.output_end(self.output.filepath)

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("http://ts.kuwo.cn/service/getlist.v31.php?act=cat&id=50")