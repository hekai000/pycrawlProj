#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import scrapy
from scrapy import log
from scrapy.http import Request
from selfwoaidu_crawl.utils.select_result import list_first_item
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class selfWoaiduBookFile(FilesPipeline):
    """
        this is for download the book covor image and then complete the 
        book_covor_image_path field to the picture's path in the file system.
    """
    # def __init__(self, store_uri, download_func=None):
    #     self.images_store = store_uri
    #     super(selfWoaiduCoverImage, self).__init__(store_uri, download_func=None)
    files_store=get_project_settings().get('FILES_STORE')

    def get_media_requests(self, item, info):
        if item.get("novelDownloadInfo"):
            download_url = list_first_item(item["novelDownloadInfo"])
            yield scrapy.Request(download_url)

    def file_path(self, request, response=None, info=None):
        # """
        # 重命名模块
        # """
        path = os.path.join(self.files_store, ''.join([request.url.replace('//', '_').replace('/', '_').replace(':', '_').replace('.', '_').replace('__','_'), '.zip']))
        print path
        return path
