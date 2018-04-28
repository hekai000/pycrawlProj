# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import time
from crawlMovie.DataOutput import DataOutput
from crawlMovie.HTMLDownloader import HTMLDownloader
from crawlMovie.MyHTMLParser import MyHTMLParser

class SpiderMan(object):
    def __init__(self):
        self.downloader = HTMLDownloader()
        self.parser = MyHTMLParser()
        self.output = DataOutput()


    def crawl(self, root_url):
        response = self.downloader.download(root_url)
        film_url_list = self.parser.parser_url(response)
        for film_url in film_url_list:
            try:
                print "11111111111"
                t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
                print "2222222222"
                print "film_url-->", film_url
                rank_url = 'http://service.library.mtime.com/Movie.api'\
                            '?Ajax_CallBack=true'\
                            '&Ajax_CallBackType=Mtime.Library.Services'\
                            '&Ajax_CallBackMethod=GetMovieOverviewRating'\
                            '&Ajax_CrossDomain=1'\
                            '&Ajax_RequestUrl=%s'\
                            '&t=%s'\
                            '&Ajax_CallBackArgument0=%s' % (film_url[0], t, film_url[1])
                print "33333[%s]" % rank_url
                rank_content = self.downloader.download(rank_url)
                print "4444444444[%s]" % rank_content
                data = self.parser.parser_json(rank_url, rank_content)
                print "555555555"
                self.output.store_data(data)
                print "6666666666666"
            except Exception as e:
                print "Crawl failed[%s]" % str(e)
        self.output.output_end()
        print "crawl finished"

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl('http://theater.mtime.com/China_Beijing/')