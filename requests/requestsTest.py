# -*- coding: utf-8 -*-

import requests
import chardet

def testReq1():
    url = "http://www.baidu.com"
    r = requests.get(url)
    print r.content
    print r.text
    print r.encoding
    r.encoding = 'utf-8'
    print r.text


    print chardet.detect(r.content)

def testReq2():
    payload = {'Keywords': 'blog:qiyeboy', 'pageindex': 1}
    r = requests.get("http://zzk.cnblogs.com/s/blogpost", params=payload)
    print r.url


def testReqHeader():
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
    headers = {'User-Agent': user_agent}
    r = requests.get("http://www.baidu.com")
    if r.status_code == requests.codes.ok:
        print r.status_code
        print r.headers
        print r.headers.get('content-type')
    else:
        r.raise_for_status()


def testSesion():
    s = requests.Session()
    url = "http://www.baidu.com"
    r = s.get(url, allow_redirects= True)
    datas = {}
    r = s.post(url, data=datas, allow_redirects=True)
if __name__ == "__main__":
    testReqHeader()
