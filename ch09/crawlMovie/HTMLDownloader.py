# -*- coding: utf-8 -*-

import requests


class HTMLDownloader(object):


    def download(self, url):
        if url is None:
            return None
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        headers = {"User-Agent": user_agent}
        r = requests.get(url, headers=headers, verify=False)
        if r.status_code ==200:
            r.encoding = "utf-8"
            return r.text
        return None