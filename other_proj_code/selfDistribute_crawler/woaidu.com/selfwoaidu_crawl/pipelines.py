# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from items import SelfwoaiduCrawlDetailItem, SelfwoaiduCrawlSimpleItem
import re
class SelfwoaiduCrawlPipeline(object):
    def __init__(self, mongo_uri, mongo_db, replicaset):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.replicaset =replicaset


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'woaidu'),
            replicaset = crawler.settings.get('REPLICASET')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri,replicaset=self.replicaset)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        if isinstance(item,SelfwoaiduCrawlSimpleItem):
            self._process_booklist_item(item)
        else:
            self._process_bookeDetail_item(item)
        return item



    def _process_booklist_item(self,item):
        '''
        处理小说信息
        :param item:
        :return:
        '''


        self.db.bookInfo.insert(dict(item))

    def _process_bookeDetail_item(self,item):
        '''
        处理小说作者
        :param item:
        :return:
        '''
        # 从novelLink中获取novelId
        pattern = re.compile('\d+')
        novelLink = item['novelLink'].strip().replace('\n','') if item['novelLink'] else ""

        match = pattern.search(novelLink)
        novelId = match.group() if match else novelLink
        item['novelId'] = novelId

        # 从novelAuthor中获取小说作者名

        novelAuthor_s = item['novelAuthor'].strip().replace('\n','') if item['novelAuthor'] else ""
        pattern = re.compile(u"：")
        match = pattern.split(novelAuthor_s)
        novelAuthor_after = match[1] if match else ""

        item['novelAuthor'] = novelAuthor_after

        self.db.bookDetail.insert(dict(item))
