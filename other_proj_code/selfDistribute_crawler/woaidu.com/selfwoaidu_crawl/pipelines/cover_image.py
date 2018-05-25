#!/usr/bin/python
#-*-coding:utf-8-*-

import os
from scrapy import log
from scrapy.http import Request
# from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.pipelines.images import ImagesPipeline
from selfwoaidu_crawl.utils.select_result import list_first_item
from scrapy.utils.project import get_project_settings

class selfWoaiduCoverImage(ImagesPipeline):
    """
        this is for download the book covor image and then complete the 
        book_covor_image_path field to the picture's path in the file system.
    """
    # def __init__(self, store_uri, download_func=None):
    #     self.images_store = store_uri
    #     super(selfWoaiduCoverImage, self).__init__(store_uri, download_func=None)
    images_store=get_project_settings().get('IMAGES_STORE')
    def get_media_requests(self, item, info):
        if item.get('novelImage'):
            yield Request(item['novelImage'], dont_filter=True)

    def item_completed(self, results, item, info):
        if self.LOG_FAILED_RESULTS:
            msg = '%s found errors proessing %s' % (self.__class__.__name__, item)
            for ok, value in results:
                if not ok:
                    log.err(value, msg, spider=info.spider)

        image_paths = [x['path'] for ok, x in results if ok]
        image_path = list_first_item(image_paths)
        if image_path:
            item['novelImagePath'] = os.path.join(os.path.abspath(self.images_store),image_path)

        return item
